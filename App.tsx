import React, { useState } from 'react';
import { GameState, Question, AnswerRecord } from './types';
import { VOCABULARY_LIST } from './constants';
import { generateQuiz } from './utils';
import StartScreen from './components/StartScreen';
import QuizScreen from './components/QuizScreen';
import ResultScreen from './components/ResultScreen';

const App: React.FC = () => {
  const [gameState, setGameState] = useState<GameState>(GameState.MENU);
  const [questions, setQuestions] = useState<Question[]>([]);
  const [results, setResults] = useState<AnswerRecord[]>([]);

  const handleStart = (count: number) => {
    const newQuestions = generateQuiz(VOCABULARY_LIST, count);
    setQuestions(newQuestions);
    setGameState(GameState.PLAYING);
    window.scrollTo(0, 0);
  };

  const handleFinish = (records: AnswerRecord[]) => {
    setResults(records);
    setGameState(GameState.RESULT);
    window.scrollTo(0, 0);
  };

  const handleRestart = () => {
    setGameState(GameState.MENU);
    setQuestions([]);
    setResults([]);
    window.scrollTo(0, 0);
  };

  return (
    <div className="bg-gray-100 min-h-screen font-sans text-gray-900">
      {gameState === GameState.MENU && (
        <StartScreen onStart={handleStart} />
      )}
      {gameState === GameState.PLAYING && (
        <QuizScreen questions={questions} onFinish={handleFinish} />
      )}
      {gameState === GameState.RESULT && (
        <ResultScreen records={results} onRestart={handleRestart} />
      )}
    </div>
  );
};

export default App;
