import "./styles.css";
import { NewCard } from "./Components/NewCard";
import { useEffect, useState } from "react";
import lucas from "./assets/NEI.jpg";

export default function App() {
  const [data, setData] = useState([]);

  const url =
    "https://saurav.tech/NewsAPI/top-headlines/category/technology/in.json";

  useEffect(() => {
    fetch(url)
      .then((response) => {
        response.json().then((news) => {
          setData(news.articles);
        });
      })
      .catch((error) => console.log(error));
  }, []);

  return (
    <div className="App">
      <h1>My news website</h1>
      <div className="news-grid">
        {data.map((article, index) => {
          return (
            <NewCard
              key={index}
              title={article.title}
              content={article.description}
              imgSrc={article.urlToImage}
            />
          );
        })}
      </div>
    </div>
  );
}
