// features/customer/customerSlice.js
import { createSlice } from "@reduxjs/toolkit";

const initialState = {
    name: "",
    email: "",
    city: "",
    district: "",
    address: "",
};

const customerSlice = createSlice({
    name: "customer",
    initialState,
    reducers: {
        // 更新單一欄位
        updateCustomer: (state, action) => {
            return { ...state, ...action.payload };
        },
        // 重置表單
        resetCustomer: () => initialState,
    },
});

export const { updateCustomer, resetCustomer } = customerSlice.actions;

export default customerSlice.reducer;
