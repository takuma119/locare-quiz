export interface TermData {
  term: string;
  meaning: string;
  category: string;
}

export interface Question extends TermData {
  options: string[]; // 4 choices including the correct one
}

export interface AnswerRecord {
  question: TermData;
  selectedOption: string;
  isCorrect: boolean;
}

export enum GameState {
  MENU = 'MENU',
  PLAYING = 'PLAYING',
  RESULT = 'RESULT',
}
