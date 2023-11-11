import { NavLink } from "react-router-dom";

function NavBar() {
    return (
        <nav>
            <NavLink to="/">About</NavLink>
            <NavLink to="/">Generate</NavLink>
            <NavLink to="/">Wizard</NavLink>
            <NavLink to="/">Game</NavLink>
            <NavLink to="/">Q&A</NavLink>
        </nav>
    )
}

export default NavBar;