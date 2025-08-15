import React from "react";
import { useSelector, useDispatch } from "react-redux";
import { decrementByproduct, incrementByproduct } from "./cartSlice";

export function Cart() {
    const countMacaron = useSelector((state) => state.cart.Macaron);
    const countCookie = useSelector((state) => state.cart.Cookie);
    const countCakeRoll = useSelector((state) => state.cart.CakeRoll);
    const dispatch = useDispatch();

    return (
        <>
            <div>
                <h2>馬卡龍</h2>
                <div>
                    <button
                        aria-label="Increment value"
                        onClick={() => dispatch(incrementByproduct("Macaron"))}
                    >
                        Increment
                    </button>
                    <span>{countMacaron}</span>
                    <button
                        aria-label="Decrement value"
                        onClick={() => dispatch(decrementByproduct("Macaron"))}
                    >
                        Decrement
                    </button>
                </div>
            </div>
            <div>
                <h2>餅乾</h2>
                <div>
                    <button
                        aria-label="Increment value"
                        onClick={() => dispatch(incrementByproduct("Cookie"))}
                    >
                        Increment
                    </button>
                    <span>{countCookie}</span>
                    <button
                        aria-label="Decrement value"
                        onClick={() => dispatch(decrementByproduct("Cookie"))}
                    >
                        Decrement
                    </button>
                </div>
            </div>
            <div>
                <h2>蛋糕捲</h2>
                <div>
                    <button
                        aria-label="Increment value"
                        onClick={() => dispatch(incrementByproduct("CakeRoll"))}
                    >
                        Increment
                    </button>
                    <span>{countCakeRoll}</span>
                    <button
                        aria-label="Decrement value"
                        onClick={() => dispatch(decrementByproduct("CakeRoll"))}
                    >
                        Decrement
                    </button>
                </div>
            </div>
        </>
    );
}
