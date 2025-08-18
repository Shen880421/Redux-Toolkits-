import { useSelector, useDispatch } from "react-redux";
import { useState, useEffect } from "react";
import { updateCustomer } from "../features/customer/customerSlice";

export default function CartCheckout() {
    const cartItems = useSelector((state) => state.cart.CartList);
    const products = useSelector((state) => state.cart);
    const customer = useSelector((state) => state.customer);
    const dispatch = useDispatch();

    const totalPrice = Object.entries(cartItems).reduce(
        (total, [name, count]) => total + count * (products[name]?.price ?? 0),
        0
    );

    // 縣市 & 行政區資料
    const [addressData, setAddressData] = useState([]);
    const [districts, setDistricts] = useState([]);

    useEffect(() => {
        const loadData = async () => {
            const res = await fetch("/data/CityCountyData.json");
            const data = await res.json();
            setAddressData(data);
        };
        loadData();
    }, []);

    const handleChange = (e) => {
        const { name, value } = e.target;
        dispatch(updateCustomer({ [name]: value }));
    };

    const handleCityChange = (e) => {
        const cityName = e.target.value;
        dispatch(updateCustomer({ city: cityName, district: "" }));
        const city = addressData.find((c) => c.CityName === cityName);
        setDistricts(city ? city.AreaList : []);
    };

    const handleDistrictChange = (e) => {
        dispatch(updateCustomer({ district: e.target.value }));
    };

    const handleCheckout = () => {
        // 產生訂單編號 (時間戳)
        const orderId = `ORD${Date.now()}`;

        // 產生綠界要求格式的交易日期 yyyy/MM/dd HH:mm:ss
        const now = new Date();
        const tradeDate = now
            .toISOString()
            .slice(0, 19)
            .replace("T", " ")
            .replace(/-/g, "/");

        // 產生商品名稱字串
        const itemNames = Object.entries(cartItems)
            .filter(([_, count]) => count > 0)
            .map(([name, count]) => `${name} x${count}`)
            .join("#");

        // 建立 form 並 POST
        const form = document.createElement("form");
        form.method = "POST";
        form.action =
            "https://payment-stage.ecpay.com.tw/Cashier/AioCheckOut/V5"; // 測試環境

        const params = {
            MerchantID: "2000132", // 測試商店代號
            MerchantTradeNo: orderId,
            MerchantTradeDate: tradeDate,
            PaymentType: "aio",
            TotalAmount: totalPrice + 80, // 加運費
            TradeDesc: "購物車訂單",
            ItemName: itemNames,
            ReturnURL: "https://你的網站/return", // 可填任意網址測試
            ChoosePayment: "Credit", // 信用卡
            ClientBackURL: "https://你的網站/cart",
            Email: customer.email,
        };

        Object.keys(params).forEach((key) => {
            const input = document.createElement("input");
            input.type = "hidden";
            input.name = key;
            input.value = params[key];
            form.appendChild(input);
        });

        document.body.appendChild(form);
        form.submit();
    };

    return (
        <div className="flex flex-col items-center p-4 w-full">
            <h2 className="text-4xl font-bold mb-6">購物車結帳</h2>

            {/* 客戶資訊 */}
            <div className="w-1/2 space-y-4 mb-6">
                <input
                    type="text"
                    name="name"
                    placeholder="姓名"
                    value={customer.name}
                    onChange={handleChange}
                    className="w-full border px-3 py-2 rounded"
                />
                <input
                    type="email"
                    name="email"
                    placeholder="Email"
                    value={customer.email}
                    onChange={handleChange}
                    className="w-full border px-3 py-2 rounded"
                />

                {/* 縣市 */}
                <select
                    name="city"
                    value={customer.city}
                    onChange={handleCityChange}
                    className="w-full border px-3 py-2 rounded"
                >
                    <option value="">---請選擇縣市---</option>
                    {addressData.map((city) => (
                        <option key={city.CityName} value={city.CityName}>
                            {city.CityName}
                        </option>
                    ))}
                </select>

                {/* 行政區 */}
                <select
                    name="district"
                    value={customer.district}
                    onChange={handleDistrictChange}
                    className="w-full border px-3 py-2 rounded"
                    disabled={!customer.city}
                >
                    <option value="">---請先選擇縣市---</option>
                    {districts.map((d) => (
                        <option key={d.AreaName} value={d.AreaName}>
                            {d.AreaName}
                        </option>
                    ))}
                </select>

                {/* 地址 */}
                <input
                    type="text"
                    name="address"
                    placeholder="地址"
                    value={customer.address}
                    onChange={handleChange}
                    className="w-full border px-3 py-2 rounded"
                />
            </div>

            {/* 訂單摘要 */}
            <div className="w-1/2 border p-4 rounded mb-6">
                <h3 className="font-semibold mb-2">訂單摘要</h3>
                <div className="flex justify-between font-bold mt-2">
                    <span>小計：</span>
                    <span>NT${totalPrice.toLocaleString()}</span>
                </div>
                <div className="flex justify-between font-bold mt-2">
                    <span>運費</span>
                    <span>NT$80</span>
                </div>
                <div className="flex justify-between font-bold mt-2">
                    <span>總計</span>
                    <span>NT${totalPrice + 80}</span>
                </div>
            </div>

            {/* 前往付款按鈕 */}
            <button
                onClick={handleCheckout}
                className="w-1/2 bg-violet-500 hover:bg-violet-700 text-white py-2 rounded text-lg"
            >
                前往付款
            </button>
        </div>
    );
}
