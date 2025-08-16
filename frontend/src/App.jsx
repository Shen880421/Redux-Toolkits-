import { useState } from "react";
import { Routes, Route } from "react-router-dom";
import Navbar from "./component/Navbar.jsx";
import Cart from "./page/cart.jsx";
import Hero from "./component/Hero.jsx";
import Footer from "./component/Footer.jsx";
import CartList from "./page/CartList.jsx";

function App() {
    const [count, setCount] = useState(0);

    return (
        <>
            <Navbar />
            <Hero />
            <Routes>
                <Route path="/" element={<Cart />} />
                <Route path="/cartlist" element={<CartList />} />
            </Routes>
            <Footer />
        </>
    );
}

export default App;
