import { useState } from "react";
import lucas from "../../assets/meMiami.jpeg";
import { Button } from "../Button";

export const NewCard = ({ imgSrc, title, content }) => {
  const [showMore, setShowMore] = useState(false);

  const getDescription = () => {
    if (showMore) {
      return content;
    } else {
      return content.slice(0, 100) + "...";
    }
  };
  return (
    <div className="news-card">
      <img src={imgSrc} alt="news illustration" />
      <div className="news-card-info">
        <h3>{title}</h3>
        <p>{getDescription()}</p>
        {content.length >= 100 && (
          <Button
            text={showMore ? "Show less" : "Click to see more"}
            variant="secondary"
            onClick={() => setShowMore(!showMore)}
          />
        )}
      </div>
    </div>
  );
};
