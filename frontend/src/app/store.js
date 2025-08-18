import { configureStore } from "@reduxjs/toolkit";
import cartReducer from "../features/cart/cartSlice";
import customerReducer from "../features/customer/customerSlice";

export const store = configureStore({
    reducer: {
        cart: cartReducer,
        customer: customerReducer,
    },
});
