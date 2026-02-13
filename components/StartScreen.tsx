import React, { useState } from 'react';
import { BookOpen, Brain, Play } from 'lucide-react';
import { VOCABULARY_LIST } from '../constants';

interface StartScreenProps {
  onStart: (count: number) => void;
}

const StartScreen: React.FC<StartScreenProps> = ({ onStart }) => {
  const maxQuestions = VOCABULARY_LIST.length;
  const [questionCount, setQuestionCount] = useState<number>(10);

  return (
    <div className="flex flex-col items-center justify-center min-h-screen p-4">
      <div className="bg-white p-8 rounded-2xl shadow-xl max-w-lg w-full text-center">
        <div className="flex justify-center mb-6">
          <div className="bg-indigo-100 p-4 rounded-full">
            <BookOpen className="w-12 h-12 text-indigo-600" />
          </div>
        </div>
        
        <h1 className="text-3xl font-bold text-gray-800 mb-2">BizTerm Master</h1>
        <p className="text-gray-500 mb-8">
          ビジネス用語・IT用語の理解度をテストしましょう。
          <br />
          全{maxQuestions}単語からランダムに出題されます。
        </p>

        <div className="mb-8 text-left bg-gray-50 p-6 rounded-xl border border-gray-100">
          <label className="block text-sm font-medium text-gray-700 mb-3 flex items-center gap-2">
            <Brain className="w-4 h-4" />
            問題数を選択 ({questionCount}問)
          </label>
          <input
            type="range"
            min="5"
            max={maxQuestions}
            step="1"
            value={questionCount}
            onChange={(e) => setQuestionCount(Number(e.target.value))}
            className="w-full h-2 bg-gray-200 rounded-lg appearance-none cursor-pointer accent-indigo-600"
          />
          <div className="flex justify-between text-xs text-gray-400 mt-2">
            <span>5問</span>
            <span>{Math.floor(maxQuestions / 2)}問</span>
            <span>{maxQuestions}問 (全問)</span>
          </div>
        </div>

        <button
          onClick={() => onStart(questionCount)}
          className="w-full bg-indigo-600 hover:bg-indigo-700 text-white font-bold py-4 px-8 rounded-xl transition-all duration-200 transform hover:scale-[1.02] active:scale-[0.98] flex items-center justify-center gap-2 shadow-lg shadow-indigo-200"
        >
          <Play className="w-5 h-5 fill-current" />
          テストを開始する
        </button>
      </div>
    </div>
  );
};

export default StartScreen;
