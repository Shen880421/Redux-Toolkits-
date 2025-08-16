import { useSelector, useDispatch } from "react-redux";
import { removeProduct } from "../features/cart/cartSlice";
export default function CartList() {
    const cartItems = useSelector((state) => state.cart.CartList);
    const products = useSelector((state) => state.cart);
    const dispatch = useDispatch();
    return (
        <div className="flex flex-col items-center p-4 mb-100 mt-30 w-full">
            <h2 className="text-6xl font-bold text-slate-950 mb-10">購物車</h2>
            <div className="flex flex-col w-1/2 space-y-10 mt-20 ">
                {Object.entries(cartItems).map(([name, count]) => (
                    <div
                        key={name}
                        className="flex flex-row justify-between items-center"
                    >
                        {name === "Macaron" && (
                            <div className="flex items-center">
                                <img
                                    src="img/orachocomacaroon.jpg"
                                    alt="馬卡龍"
                                    className="object-cover w-20 h-20 shadow-xl/30 opacity-80 inset-shadow-indigo-500 mr-5"
                                />
                                <p>馬卡龍: {count.num}</p>
                            </div>
                        )}
                        {name === "Cookie" && (
                            <div className="flex items-center">
                                <img
                                    src="img/caramelbuttercookie-1-1.jpg"
                                    alt="焦糖奶油餅乾"
                                    className="object-cover w-20 h-20 shadow-xl/30 opacity-80 inset-shadow-indigo-500 mr-5"
                                />
                                <p>焦糖奶油餅乾: {count.num}</p>
                            </div>
                        )}
                        {name === "CakeRoll" && (
                            <div className="flex items-center">
                                <img
                                    src="img/vanilacakeroll.jpg"
                                    alt="香草蛋糕捲"
                                    className="object-cover w-20 h-20 shadow-xl/30 opacity-80 inset-shadow-indigo-500 mr-5"
                                />
                                <p>香草蛋糕捲: {count.num}</p>
                            </div>
                        )}

                        <div className="flex flex-row items-center">
                            <div className="mr-2">{count} 個</div>
                            <div>總金額: {count * products[name].price} 元</div>
                            <button
                                className="bg-amber-500 hover:bg-amber-700 text-white font-bold py-2 px-4 rounded"
                                onClick={() => dispatch(removeProduct(name))}
                            >
                                移除
                            </button>
                        </div>
                    </div>
                ))}
            </div>
        </div>
    );
}
