import React from "react";
import { useSelector, useDispatch } from "react-redux";
import {
    decrementByproduct,
    incrementByproduct,
    addToCartList,
} from "../features/cart/cartSlice";
import { useNavigate } from "react-router-dom";

export default function Cart() {
    const products = useSelector((state) => state.cart);
    const dispatch = useDispatch();
    const navigate = useNavigate();

    const handleAddToCart = () => {
        // Dispatch an action to add the item to the cart
        dispatch(
            addToCartList({
                MacaronNum: products.Macaron.num,
                CookieNum: products.Cookie.num,
                CakeRollNum: products.CakeRoll.num,
            })
        );
        navigate("/cartlist");
    };

    return (
        <div className="flex flex-col items-center">
            <div className="p-4 flex flex-row justify-center w-full gap-20 mt-30">
                <div className="flex flex-col items-center">
                    <img
                        src="img/orachocomacaroon.jpg"
                        alt="馬卡龍"
                        className="object-cover w-40 h-40 shadow-xl/30 opacity-80 inset-shadow-indigo-500"
                    />
                    <h2>馬卡龍</h2>
                    <div className="flex flex-row gap-5">
                        價格: {products.Macaron.price}
                    </div>
                    <div className="flex flex-row gap-5">
                        <button
                            aria-label="Increment value"
                            onClick={() =>
                                dispatch(incrementByproduct("Macaron"))
                            }
                        >
                            <img
                                src="img/plus.png"
                                alt="+"
                                className="w-6 h-6"
                            />
                        </button>
                        <div>數量: {products.Macaron.num}</div>
                        <button
                            aria-label="Decrement value"
                            onClick={() =>
                                dispatch(decrementByproduct("Macaron"))
                            }
                        >
                            <img
                                src="img/minus.png"
                                alt="-"
                                className="w-6 h-6"
                            />
                        </button>
                    </div>
                </div>
                <div className="flex flex-col items-center">
                    <img
                        src="img/caramelbuttercookie-1-1.jpg"
                        alt="焦糖奶油餅乾"
                        className="object-cover w-40 h-40 shadow-xl/30 opacity-80 inset-shadow-indigo-500"
                    />
                    <h2>焦糖奶油餅乾</h2>
                    <div className="flex flex-row gap-5">
                        價格: {products.Cookie.price}
                    </div>
                    <div className="flex flex-row gap-5">
                        <button
                            aria-label="Increment value"
                            onClick={() =>
                                dispatch(incrementByproduct("Cookie"))
                            }
                        >
                            <img
                                src="img/plus.png"
                                alt="+"
                                className="w-6 h-6"
                            />
                        </button>
                        <div>數量: {products.Cookie.num}</div>
                        <button
                            aria-label="Decrement value"
                            onClick={() =>
                                dispatch(decrementByproduct("Cookie"))
                            }
                        >
                            <img
                                src="img/minus.png"
                                alt="-"
                                className="w-6 h-6"
                            />
                        </button>
                    </div>
                </div>
                <div className="flex flex-col items-center">
                    <img
                        src="img/vanilacakeroll.jpg"
                        alt="香草蛋糕捲"
                        className="object-cover w-40 h-40 shadow-xl/30 opacity-80 inset-shadow-indigo-500"
                    />
                    <h2>香草蛋糕捲</h2>
                    <div className="flex flex-row gap-5">
                        價格: {products.CakeRoll.price}
                    </div>
                    <div className="flex flex-row gap-5">
                        <button
                            aria-label="Increment value"
                            onClick={() =>
                                dispatch(incrementByproduct("CakeRoll"))
                            }
                        >
                            <img
                                src="img/plus.png"
                                alt="+"
                                className="w-6 h-6"
                            />
                        </button>
                        <div>數量: {products.CakeRoll.num}</div>
                        <button
                            aria-label="Decrement value"
                            onClick={() =>
                                dispatch(decrementByproduct("CakeRoll"))
                            }
                        >
                            <img
                                src="img/minus.png"
                                alt="-"
                                className="w-6 h-6"
                            />
                        </button>
                    </div>
                </div>
            </div>
            <button
                className="bg-teal-200 hover:bg-teal-500 text-cyan-900 hover:text-slate-100 py-2 px-4 rounded w-5/6 mt-30"
                onClick={handleAddToCart}
            >
                加入購物車
            </button>
        </div>
    );
}
