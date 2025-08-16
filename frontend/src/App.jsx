import { useState } from "react";
import Navbar from "./component/Navbar.jsx";
import Car from "./features/cart/cart.jsx";

function App() {
    const [count, setCount] = useState(0);

    return (
        <>
            <Navbar />
            <Car />
        </>
    );
}

export default App;
