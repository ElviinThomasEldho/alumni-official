import React, { useState, useEffect } from 'react';
import Navbar from './components/Navbar';
import MainCard from './components/mainCard';
import ProfileRightCard from './components/ProfileRightCard';
import axios from 'axios';

const App = () => {
  const [token, setToken] = useState("");
  const [posts, setPosts] = useState([]);

  useEffect(() => {
    axios
      .post("http://localhost:8000/api/login/", { "username": "vijaykv", "password": "admin1234@" })
      .then(res => {
        console.log(res.data);
        setToken(res.data.token);
      })
      .catch(err => console.log("Error :", err));
  }, []);

  useEffect(() => {
    if (token) {
      const config = { headers: { 'Authorization': 'token ' + token } };
      axios
        .get("http://127.0.0.1:8000/api/get-feed-posts/", config)
        .then(res => {
          if (Array.isArray(res.data)) {
            setPosts(res.data);
            console.log(res.data);
          }
        })
        .catch(err => console.log(err));
    }
  }, [token]);

  return (
    <div>
    <h1>Hi</h1>
      <Navbar />
      <div className=' h-fit flex'>
        <div className="w-1/5 h-full flex flex-col pt-12 items-center rounded-lg mx-12 my-9">
          <img
            src="https://i.ibb.co/68Vymy9/aeecc22a67dac7987a80ac0724658493.jpg"
            alt="Profile"
            className="w-16 h-16 rounded-full mb-4"
          />
          <h2 className="text-xl font-semibold">Welcome, User! </h2>
        </div>
        <div className='flex flex-col'>
          {Array.isArray(posts) && posts.map(post => <MainCard key={post.id} token={token} post={post} />)}
        </div>
        <ProfileRightCard />
      </div>
    </div>
  );
};

export default App;
