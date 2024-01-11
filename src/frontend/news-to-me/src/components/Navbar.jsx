import React from "react";
import { Link } from "react-router-dom";
import { NavLink } from "react-router-dom";
import logo from "../imgs/Logo.jpg";

/**
 * Define the Navbar component
 * @returns {JSX.Element} - The Navbar component.
 */
export const Navbar = () => {
  return (
    <nav className="flex items-center justify-between bg-gradient-to-r from-slate-800 to-slate-700 font-bold shadow-inner border-b">
      <div className="justify-between items-center flex">
        <img src={logo} className="ml-2 w-12 h-12 rounded-b-xl mr-2" />
        <Link to="/" className=" text-white text-center text-4xl">
          NewsToMe
        </Link>
      </div>

      <ul className="flex justify-between text-center p-5">
        <li className="">
          <NavLink
            to="/About"
            className="p-2 m-2 text-white rounded-lg hover:bg-black active:bg-indigo-600"
            activeClassname="bg-indigo-600"
          >
            About
          </NavLink>
        </li>
        
      </ul>
    </nav>
  );
};

export default Navbar;