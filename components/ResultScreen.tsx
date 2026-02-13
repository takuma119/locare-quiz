import React from 'react';
import { AnswerRecord } from '../types';
import { Trophy, RefreshCw, CheckCircle2, XCircle } from 'lucide-react';

interface ResultScreenProps {
  records: AnswerRecord[];
  onRestart: () => void;
}

const ResultScreen: React.FC<ResultScreenProps> = ({ records, onRestart }) => {
  const correctCount = records.filter((r) => r.isCorrect).length;
  const totalCount = records.length;
  const percentage = Math.round((correctCount / totalCount) * 100);

  let message = "";
  if (percentage === 100) message = "完璧です！素晴らしい！";
  else if (percentage >= 80) message = "すごい！高得点です！";
  else if (percentage >= 60) message = "その調子！あと少しです。";
  else message = "次はもっと頑張ろう！";

  return (
    <div className="min-h-screen bg-gray-50 p-4 md:p-8">
      <div className="max-w-3xl mx-auto">
        <div className="bg-white rounded-3xl shadow-xl overflow-hidden mb-8">
          <div className="bg-indigo-600 p-8 text-center text-white">
            <Trophy className="w-16 h-16 mx-auto mb-4 text-yellow-300" />
            <h1 className="text-3xl font-bold mb-2">結果発表</h1>
            <div className="text-6xl font-black mb-2 tracking-tighter">
              {percentage}<span className="text-3xl font-medium">%</span>
            </div>
            <p className="text-indigo-200 text-lg">
              {totalCount}問中 {correctCount}問正解
            </p>
            <p className="mt-4 font-bold text-xl">{message}</p>
          </div>

          <div className="p-6">
            <button
              onClick={onRestart}
              className="w-full bg-gray-900 hover:bg-gray-800 text-white font-bold py-4 rounded-xl transition-all flex items-center justify-center gap-2 shadow-lg"
            >
              <RefreshCw className="w-5 h-5" />
              もう一度挑戦する
            </button>
          </div>
        </div>

        <h3 className="text-xl font-bold text-gray-800 mb-4 px-2">振り返り</h3>
        <div className="space-y-4">
          {records.map((record, idx) => (
            <div 
              key={idx} 
              className={`bg-white p-5 rounded-xl shadow-sm border-l-4 ${
                record.isCorrect ? 'border-green-500' : 'border-red-500'
              }`}
            >
              <div className="flex items-start gap-3">
                <div className="mt-1 flex-shrink-0">
                  {record.isCorrect ? (
                    <CheckCircle2 className="w-6 h-6 text-green-500" />
                  ) : (
                    <XCircle className="w-6 h-6 text-red-500" />
                  )}
                </div>
                <div className="flex-grow">
                  <div className="flex justify-between items-start mb-2">
                    <span className="text-xs font-semibold text-gray-400 uppercase tracking-wider">
                      Q.{idx + 1} {record.question.category}
                    </span>
                  </div>
                  <p className="text-gray-800 font-medium mb-3">
                    {record.question.meaning}
                  </p>
                  
                  <div className="flex flex-col sm:flex-row gap-2 sm:gap-8 text-sm">
                    <div className="flex flex-col">
                      <span className="text-gray-400 text-xs">正解</span>
                      <span className="font-bold text-green-700">{record.question.term}</span>
                    </div>
                    {!record.isCorrect && (
                      <div className="flex flex-col">
                        <span className="text-gray-400 text-xs">あなたの回答</span>
                        <span className="font-bold text-red-600 line-through decoration-red-400 decoration-2">
                          {record.selectedOption}
                        </span>
                      </div>
                    )}
                  </div>
                </div>
              </div>
            </div>
          ))}
        </div>
        
        <div className="h-12"></div> {/* Spacer */}
      </div>
    </div>
  );
};

export default ResultScreen;
