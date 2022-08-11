import React from 'react';

export default function Header(props) {
  return (
    <header className="block row center">
      <div>
          <h1>
            <img src = "http://burritobuilders.letseat.at/system/business_logos/17737/original/5aac016782ab663fdb9e.jpg?1384665485"
            />
          </h1>
      </div>
      <div>
        <a href="#/cart">
           
          Cart{' '}
          {props.countCartItems ? (
            <button className="badge">{props.countCartItems}</button>
          ) : (
            ''
          )}
        </a>{' '}
      </div>
    </header>
  );
}