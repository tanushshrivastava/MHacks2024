import React from 'react';
import { Link } from 'react-scroll';

const Header = () => {
    return (
        <header style={{ background: '#333', color: '#fff', padding: '10px 20px', textAlign: 'center' }}>
            <h1>My Website</h1>
            <nav>
                <Link to="section1" smooth={true} duration={1000}>Section 1</Link> |
                <Link to="section2" smooth={true} duration={1000}>Section 2</Link> |
                <Link to="section3" smooth={true} duration={1000}>Section 3</Link>
            </nav>
        </header>
    );
};

export default Header;
