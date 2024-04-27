import React from "react";

const Progress: React.FC<{progress: number}> = ({progress}) => {
    const radius = 35;
    const circumference = 2 * Math.PI * radius;
    const strokeOffset = (1 / 4) * circumference;
    const strokeDasharray = progress * circumference;

    return (
        <div className="relative w-max mx-auto">
        <svg
            className="m-0 stroke-primary block fill-transparent"
            style={{
                width: "80px",
                height: "80px",
                strokeWidth: "10px",
            }}
        >
            <circle
                cx="40"
                cy="40"
                r={radius}
                strokeDashoffset={strokeOffset}
                strokeDasharray={`${strokeDasharray}, ${circumference - strokeDasharray}`}
            />
        </svg>
            <div className="text-xl absolute top-6 w-full text-center text-muted-foreground">{progress * 100}%</div>
        </div>
    );
}

export default Progress;