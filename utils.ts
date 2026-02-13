import { TermData, Question } from './types';

// Fisher-Yates shuffle
export function shuffleArray<T>(array: T[]): T[] {
  const newArray = [...array];
  for (let i = newArray.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [newArray[i], newArray[j]] = [newArray[j], newArray[i]];
  }
  return newArray;
}

export function generateQuiz(allTerms: TermData[], numberOfQuestions: number): Question[] {
  // 1. Shuffle all terms to get random questions
  const shuffledTerms = shuffleArray(allTerms);
  const selectedTerms = shuffledTerms.slice(0, numberOfQuestions);

  return selectedTerms.map((currentTerm) => {
    // 2. For each question, find 3 distractors
    // Filter out the current term to avoid duplicates
    const otherTerms = allTerms.filter(t => t.term !== currentTerm.term);
    
    // Shuffle the remaining terms and pick 3
    const shuffledDistractors = shuffleArray(otherTerms);
    const distractors = shuffledDistractors.slice(0, 3).map(d => d.term);

    // 3. Combine correct answer and distractors, then shuffle
    const options = shuffleArray([currentTerm.term, ...distractors]);

    return {
      ...currentTerm,
      options
    };
  });
}
