function Navbar() {
    return (
        <div className="bg-slate-400 flex items-center p-4 h-30">
            <img
                src="img/wannabakerylogo.jpg"
                alt="logo"
                className="h-20 w-20  mr-2"
            />
            <h1 className="text-white text-5xl text-center font-bold caveat-regular">
                WannaBackery
            </h1>
            <nav className="ml-auto flex space-x-4">
                <button className="bg-white hover:bg-slate-300 text-slate-400 hover:text-white py-1 px-4 rounded text-2xl">
                    回首頁
                </button>
                <button className="bg-white hover:bg-slate-300 text-slate-400 hover:text-white py-1 px-4 rounded text-2xl">
                    登入
                </button>
                <button className="bg-white hover:bg-slate-300 text-slate-400 hover:text-white py-1 px-4 rounded text-2xl">
                    購物車
                </button>
            </nav>
        </div>
    );
}

export default Navbar;
