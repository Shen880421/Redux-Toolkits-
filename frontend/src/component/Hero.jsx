export default function Hero() {
    return (
        <div className="bg-hero-pattern h-screen flex items-center justify-center mb-10">
            <img
                src="img/coffetime.png"
                alt="Hero Image"
                className="object-cover w-full h-full shadow-xl/30 opacity-80 inset-shadow-indigo-500"
            />
        </div>
    );
}
