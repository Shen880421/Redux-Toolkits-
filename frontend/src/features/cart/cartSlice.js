import { createSlice } from "@reduxjs/toolkit";

const initialState = {
    Macaron: 0,
    Cookie: 0,
    CakeRoll: 0,
};

export const cartSlice = createSlice({
    // Redux Toolkit allows us to write "mutating" logic in reducers. It
    // doesn't actually mutate the state because it uses the Immer library,
    // which detects changes to a "draft state" and produces a brand new
    // immutable state based off those changes
    name: "cart",
    initialState,
    reducers: {
        incrementByproduct: (state, action) => {
            const product = action.payload;
            state[product] += 1;
        },
        decrementByproduct: (state, action) => {
            const product = action.payload;
            state[product] -= 1;
        },
        incrementByAmount: (state, action) => {
            const { product, num } = action.payload;
            state[product] += num;
        },
    },
});

// Action creators are generated for each case reducer function
export const { incrementByproduct, decrementByproduct, incrementByAmount } =
    cartSlice.actions;

export default cartSlice.reducer;
