import { createSlice } from "@reduxjs/toolkit";

const initialState = {
  Macaron: { num: 0, price: 90 },
  Cookie: { num: 0, price: 30 },
  CakeRoll: { num: 0, price: 60 },
  CartList: { Macaron: 0, Cookie: 0, CakeRoll: 0 },
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
      state[product].num += 1;
    },
    decrementByproduct: (state, action) => {
      const product = action.payload;
      if (state[product].num > 0) {
        state[product].num -= 1;
      } else {
        state[product].num = 0;
      }
    },
    incrementByAmount: (state, action) => {
      const { product, n } = action.payload;
      state[product].num += n;
    },
    addToCartList: (state, action) => {
      const { MacaronNum, CookieNum, CakeRollNum } = action.payload;
      state.CartList["Macaron"] = MacaronNum;
      state.CartList["Cookie"] = CookieNum;
      state.CartList["CakeRoll"] = CakeRollNum;
    },
    removeProduct: (state, action) => {
      const name = action.payload;
      state.CartList[name] = 0;
      state[name].num = 0;
    },
  },
});

// Action creators are generated for each case reducer function
export const {
  incrementByproduct,
  decrementByproduct,
  incrementByAmount,
  addToCartList,
  removeProduct,
} = cartSlice.actions;

export default cartSlice.reducer;
