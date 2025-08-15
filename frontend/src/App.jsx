import { useState } from "react";
import { Cart } from "./features/cart/cart";

function App() {
    const [count, setCount] = useState(0);

    return (
        <>
            <Cart />
        </>
    );
}

export default App;
