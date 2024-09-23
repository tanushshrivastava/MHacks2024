import React from 'react';

const Section = ({ title, id }) => {
    return (
        <div id={id} style={{ height: '100vh', padding: '20px', background: 'lightblue', textAlign: 'center' }}>
            <h2>{title}</h2>
            <p>This is the content for {title}.</p>
        </div>
    );
};

export default Section;
