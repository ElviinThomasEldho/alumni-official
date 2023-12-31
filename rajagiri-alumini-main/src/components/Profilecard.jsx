import React from 'react';

const ProfileCard = () => {
  const name =localStorage.getItem('username')
  return (
    <div className="w-1/5 h-full flex flex-col pt-12 items-center rounded-lg mx-12 my-9">
      <img
        src="https://i.ibb.co/68Vymy9/aeecc22a67dac7987a80ac0724658493.jpg" 
        alt="Profile"
        className="w-16 h-16 rounded-full mb-4"
      />

     <h2 className="text-xl font-semibold">Welcomb,{name} </h2>
      
    </div>
  );
};

export default ProfileCard;
