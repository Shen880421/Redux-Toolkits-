import { useState } from "react";
import Navbar from "./component/Navbar.jsx";
import Car from "./features/cart/cart.jsx";
import Hero from "./component/Hero.jsx";
import Footer from "./component/Footer.jsx";

function App() {
    const [count, setCount] = useState(0);

    return (
        <>
            <Navbar />
            <Hero />
            <Car />
            <Footer />
        </>
    );
}

export default App;
