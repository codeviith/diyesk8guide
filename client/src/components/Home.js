import React, { useState, useEffect } from 'react';


const Home = () => {
    const [boards, setBoards] = useState([]);
    const [questions, setQuestions] = useState([]);
    const [posts, setPosts] = useState([]);
  
    useEffect(() => {
      // Fetch data for boards
      fetch('your-api-endpoint/boards')
        .then(response => response.json())
        .then(data => setBoards(data));
  
      // Fetch data for questions
      fetch('your-api-endpoint/questions')
        .then(response => response.json())
        .then(data => setQuestions(data));
  
      // Fetch data for posts
      fetch('your-api-endpoint/posts')
        .then(response => response.json())
        .then(data => setPosts(data));
    }, []); // Empty dependency array means this effect runs once after the initial render
  
    const handleDelete = (category, id) => {
      // Make a DELETE request to your Flask API to delete the item
      fetch(`your-api-endpoint/${category}/${id}`, {
        method: 'DELETE',
      })
        .then(response => {
          if (!response.ok) {
            throw new Error('Network response was not ok');
          }
          // Remove the deleted item from the state
          switch (category) {
            case 'boards':
              setBoards(prevBoards => prevBoards.filter(board => board.id !== id));
              break;
            case 'questions':
              setQuestions(prevQuestions => prevQuestions.filter(question => question.id !== id));
              break;
            case 'posts':
              setPosts(prevPosts => prevPosts.filter(post => post.id !== id));
              break;
            default:
              break;
          }
        })
        .catch(error => console.error('Error deleting item:', error));
    };
  
    return (
      <div>
        <div>
          <h2>Boards</h2>
          <ul>
            {boards.map(board => (
              <li key={board.id}>
                {board.name}
                <button onClick={() => handleDelete('boards', board.id)}>Delete</button>
              </li>
            ))}
          </ul>
        </div>
  
        <div>
          <h2>Questions</h2>
          <ul>
            {questions.map(question => (
              <li key={question.id}>
                {question.title}
                <button onClick={() => handleDelete('questions', question.id)}>Delete</button>
              </li>
            ))}
          </ul>
        </div>
  
        <div>
          <h2>Posts</h2>
          <ul>
            {posts.map(post => (
              <li key={post.id}>
                {post.title}
                <button onClick={() => handleDelete('posts', post.id)}>Delete</button>
              </li>
            ))}
          </ul>
        </div>
      </div>
    );
  };
  
  export default Home;