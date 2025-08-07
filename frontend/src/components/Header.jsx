import React from 'react';

function Header() {
  return (
    <div className="bg-black h-[94px] pl-[90px] pr-[90px] flex justify-between items-center">
      <a href="/">
        <img src="Help_Centre_Header.png" className="h-[32px]" alt="Help Centre Header" />
      </a>
      <a href="/signin">
        <button className="bg-purple text-white px-4 py-2 rounded font-calibre font-semibold h-[32px] hover:bg-white hover:text-purple">
          Sign in
        </button>
      </a>
    </div>
  );
};

export default Header;