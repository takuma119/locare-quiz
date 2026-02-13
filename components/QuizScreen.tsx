import React, { useState, useEffect } from 'react';
import { Question, AnswerRecord } from '../types';
import { CheckCircle2, XCircle, ArrowRight } from 'lucide-react';

interface QuizScreenProps {
  questions: Question[];
  onFinish: (records: AnswerRecord[]) => void;
}

const QuizScreen: React.FC<QuizScreenProps> = ({ questions, onFinish }) => {
  const [currentIndex, setCurrentIndex] = useState(0);
  const [selectedOption, setSelectedOption] = useState<string | null>(null);
  const [isAnswered, setIsAnswered] = useState(false);
  const [records, setRecords] = useState<AnswerRecord[]>([]);

  const currentQuestion = questions[currentIndex];
  const progress = ((currentIndex) / questions.length) * 100;

  const handleOptionClick = (option: string) => {
    if (isAnswered) return;

    setSelectedOption(option);
    setIsAnswered(true);

    const isCorrect = option === currentQuestion.term;
    const newRecord: AnswerRecord = {
      question: currentQuestion,
      selectedOption: option,
      isCorrect,
    };

    setRecords((prev) => [...prev, newRecord]);
  };

  const handleNext = () => {
    if (currentIndex < questions.length - 1) {
      setCurrentIndex((prev) => prev + 1);
      setSelectedOption(null);
      setIsAnswered(false);
    } else {
      onFinish(records);
    }
  };

  // Keyboard support for 1-4 keys? Maybe later. Keeping it simple touch/click first.

  return (
    <div className="min-h-screen flex flex-col items-center p-4 max-w-3xl mx-auto">
      {/* Progress Bar */}
      <div className="w-full h-2 bg-gray-200 rounded-full mb-6 mt-4">
        <div 
          className="h-full bg-indigo-600 rounded-full transition-all duration-500 ease-out"
          style={{ width: `${progress}%` }}
        ></div>
      </div>

      <div className="w-full flex justify-between items-center mb-6 text-sm font-medium text-gray-500">
        <span>Question {currentIndex + 1} / {questions.length}</span>
        <span className="bg-indigo-50 text-indigo-700 px-3 py-1 rounded-full text-xs">
          {currentQuestion.category}
        </span>
      </div>

      {/* Card */}
      <div className="bg-white rounded-2xl shadow-lg p-6 md:p-10 w-full mb-6 flex-grow flex flex-col justify-center">
        <h2 className="text-xl md:text-2xl font-bold text-gray-800 leading-relaxed mb-8">
          {currentQuestion.meaning}
        </h2>

        <div className="grid grid-cols-1 gap-3">
          {currentQuestion.options.map((option, idx) => {
            let buttonStyle = "border-2 border-gray-100 hover:border-indigo-200 hover:bg-indigo-50";
            let icon = null;

            if (isAnswered) {
              if (option === currentQuestion.term) {
                // Correct answer always green
                buttonStyle = "border-green-500 bg-green-50 text-green-700 font-semibold";
                icon = <CheckCircle2 className="w-5 h-5 text-green-600" />;
              } else if (option === selectedOption) {
                // Wrong selection red
                buttonStyle = "border-red-500 bg-red-50 text-red-700";
                icon = <XCircle className="w-5 h-5 text-red-600" />;
              } else {
                // Others faded
                buttonStyle = "border-gray-100 text-gray-400 opacity-50";
              }
            } else if (selectedOption === option) {
               // Selected state (before validation logic runs - effectively instantaneous here but good for structure)
               buttonStyle = "border-indigo-500 bg-indigo-50";
            }

            return (
              <button
                key={idx}
                onClick={() => handleOptionClick(option)}
                disabled={isAnswered}
                className={`w-full p-4 rounded-xl text-left transition-all duration-200 flex justify-between items-center ${buttonStyle}`}
              >
                <span className="text-lg">{option}</span>
                {icon}
              </button>
            );
          })}
        </div>
      </div>

      {/* Next Button */}
      <div className="h-20 w-full flex items-start justify-center">
        {isAnswered && (
          <button
            onClick={handleNext}
            className="bg-indigo-600 text-white font-bold py-3 px-8 rounded-full shadow-lg hover:bg-indigo-700 transition-transform transform hover:scale-105 flex items-center gap-2 animate-in fade-in slide-in-from-bottom-4 duration-300"
          >
            {currentIndex === questions.length - 1 ? '結果を見る' : '次の問題へ'}
            <ArrowRight className="w-5 h-5" />
          </button>
        )}
      </div>
    </div>
  );
};

export default QuizScreen;
