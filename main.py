import streamlit as st
import random
import time

# -----------------------------------------------------------------------------
# Data Definition
# -----------------------------------------------------------------------------

VOCABULARY_LIST = [
  { "term": "スコープ", "meaning": "プロジェクトや業務における「実施範囲」や「対象領域」のこと", "category": "ビジネス基礎" },
  { "term": "カンバン", "meaning": "タスクを「未着手」「進行中」「完了」などの状態ごとにボード上のカードとして可視化・管理する手法", "category": "ビジネス基礎" },
  { "term": "ガントチャート", "meaning": "プロジェクトのスケジュール管理表。横軸に時間、縦軸に作業項目をとり、進捗を棒グラフで可視化したもの", "category": "ビジネス基礎" },
  { "term": "クリティカルパス", "meaning": "プロジェクトの全工程の中で、遅延すると全体の納期遅れに直結する「最長の作業経路」のこと", "category": "ビジネス基礎" },
  { "term": "リードタイム", "meaning": "発注から納品まで、または作業開始から完了までにかかる所要時間", "category": "ビジネス基礎" },
  { "term": "たたき台", "meaning": "議論や検討を始めるための、とりあえずの試案・原案", "category": "ビジネス基礎" },
  { "term": "FB", "meaning": "成果物や行動に対する「評価」や「改善点の指摘」を行うこと", "category": "ビジネス基礎" },
  { "term": "ASAP", "meaning": "「できるだけ早く（As Soon As Possible）」を意味する略語", "category": "ビジネス基礎" },
  { "term": "MTG", "meaning": "「会議（Meeting）」の略称。チャットやカレンダー等で多用される", "category": "ビジネス基礎" },
  { "term": "TBD", "meaning": "「未定（To Be Determined）」の略。資料などで数値や日付がまだ決まっていない箇所に仮置きする記号", "category": "ビジネス基礎" },
  { "term": "アンラーニング", "meaning": "過去の知識や成功体験を意識的に捨て、新しい環境に適応するために学び直すこと（学習棄却）", "category": "ビジネス基礎" },
  { "term": "プロパー", "meaning": "「本来の」「正規の」を意味し、文脈により「生え抜き社員」や「正社員」を指す言葉", "category": "ビジネス基礎" },
  { "term": "ブラックボックス", "meaning": "内部の構造や仕組みが不明で、外部からは入力と出力の関係しか分からない状態", "category": "ビジネス基礎" },
  { "term": "コンフリクト", "meaning": "意見の食い違いや利害の対立、衝突のこと", "category": "ビジネス基礎" },
  { "term": "ハレーション", "meaning": "ある言動や施策が、周囲に及ぼす「悪影響」や「強い反発」のこと", "category": "ビジネス基礎" },
  { "term": "キックオフ", "meaning": "プロジェクトの開始時に行われる、メンバーの顔合わせや目標共有のための最初の会合", "category": "ビジネス基礎" },
  { "term": "フェーズ", "meaning": "プロジェクトなどの活動を時系列で区切った、それぞれの「段階」や「局面」", "category": "ビジネス基礎" },
  { "term": "イニシアチブ", "meaning": "物事を主導する「主導権」のこと", "category": "ビジネス基礎" },
  { "term": "キャッチアップ", "meaning": "遅れを取り戻すこと、または未経験の分野を急いで勉強して追いつくこと", "category": "ビジネス基礎" },
  { "term": "バジェット", "meaning": "特定の用途に割り当てられた「予算」のこと", "category": "ビジネス基礎" },
  { "term": "マター", "meaning": "担当や責任の所在を示す言葉。「営業部〇〇」のように使う", "category": "ビジネス基礎" },
  { "term": "オンスケ", "meaning": "作業が計画（スケジュール）通りに遅れなく進んでいる状態", "category": "ビジネス基礎" },
  { "term": "リスケ", "meaning": "予定していた日時や計画を変更・再調整すること", "category": "ビジネス基礎" },
  { "term": "ペンディング", "meaning": "物事を決定せず「保留」や「先送り」にすること", "category": "ビジネス基礎" },
  { "term": "フィックス", "meaning": "内容や仕様を最終的に「決定・確定」させること", "category": "ビジネス基礎" },
  { "term": "アサイン", "meaning": "仕事や役割に担当者を「任命」または「割り当て」すること", "category": "ビジネス基礎" },
  { "term": "エビデンス", "meaning": "主張や提案の根拠となる「証拠」や「裏付け」のこと", "category": "ビジネス基礎" },
  { "term": "心理的安全性", "meaning": "チーム内で「何を言っても罰せられない、拒絶されない」という安心感のこと", "category": "ビジネス基礎" },
  { "term": "キャパシティ", "meaning": "能力や収容力の限界、許容量のこと", "category": "ビジネス基礎" },
  { "term": "エンゲージメント", "meaning": "従業員の会社に対する「愛着心」や「貢献意欲」のこと", "category": "ビジネス基礎" },
  { "term": "OJT", "meaning": "実際の業務を遂行しながら、先輩や上司が仕事を教える教育手法", "category": "ビジネス基礎" },
  { "term": "リスクヘッジ", "meaning": "起こりうる危険や損失を予測して、あらかじめ回避策や備えを用意しておくこと", "category": "ビジネス基礎" },
  { "term": "ブラッシュアップ", "meaning": "企画書や資料、アイデアなどを磨き上げて、より良いものにすること", "category": "ビジネス基礎" },
  { "term": "ベストプラクティス", "meaning": "過去の事例の中で最も効果的・効率的だった実践方法や成功事例", "category": "ビジネス基礎" },
  { "term": "ナレッジ", "meaning": "組織や個人が蓄積している、有益な「知識・経験・ノウハウ」のこと", "category": "ビジネス基礎" },
  { "term": "工数", "meaning": "作業を完了させるために必要な「作業量」のこと。人月や人日などの単位で表す", "category": "ビジネス基礎" },
  { "term": "1on1", "meaning": "上司と部下が定期的に行う対話。評価ではなく、部下の成長支援や信頼関係構築を目的とする", "category": "ビジネス基礎" },
  { "term": "NDA", "meaning": "取引に際して、営業秘密や個人情報を第三者に漏らさないことを約束する「秘密保持契約」", "category": "ビジネス基礎" },
  { "term": "エスカレーション", "meaning": "トラブル時などに、上司や上位者に報告し、判断や対応を仰ぐこと", "category": "ビジネス基礎" },
  { "term": "コミット", "meaning": "結果や目標達成に対して「責任を持って約束する」こと", "category": "ビジネス基礎" },
  { "term": "インセンティブ", "meaning": "意欲を引き出すための動機付け、または成果に応じた報奨金", "category": "ビジネス基礎" },
  { "term": "コンセンサス", "meaning": "関係者の間での「合意」や「意見の一致」のこと", "category": "ビジネス基礎" },
  { "term": "コンプライアンス", "meaning": "法令遵守。法律だけでなく、社会規範や倫理を守って活動すること", "category": "ビジネス基礎" },
  { "term": "リソース", "meaning": "経営資源のこと。主にヒト・モノ・カネ・時間・情報を指す", "category": "ビジネス基礎" },
  { "term": "バッファ", "meaning": "不測の事態に備えて確保しておく、時間・予算・物資などの「余裕」や「予備」", "category": "ビジネス基礎" },
  { "term": "アジェンダ", "meaning": "会議における「検討課題」や「議題」のリスト、または行動計画", "category": "ビジネス基礎" },
  { "term": "B2C", "meaning": "企業が「一般消費者」に対して商品やサービスを提供するビジネスモデル", "category": "ビジネス基礎" },
  { "term": "ステークホルダー", "meaning": "株主、従業員、顧客、取引先など、企業の活動に関わるすべての「利害関係者」", "category": "ビジネス基礎" },
  { "term": "B2B", "meaning": "企業が「企業」に対して商品やサービスを提供するビジネスモデル", "category": "ビジネス基礎" },
  { "term": "マイルストーン", "meaning": "プロジェクトの工程における重要な「節目」や「中間目標地点」", "category": "ビジネス基礎" },
  { "term": "エンプラ", "meaning": "「エンタープライズ」の略で、大企業や中堅企業などの法人組織のこと", "category": "ビジネス基礎" },
  { "term": "SMB", "meaning": "「Small to Medium Business」の略で、中小・中堅企業のこと", "category": "ビジネス基礎" },
  { "term": "仮説思考", "meaning": "限られた情報から「仮の結論」を先に設定し、それを検証しながら問題解決を図る思考法", "category": "思考法・フレームワーク" },
  { "term": "粒度", "meaning": "物事の細かさや詳細度のレベル（グレニュラリティ）", "category": "思考法・フレームワーク" },
  { "term": "マスト / ウォント", "meaning": "「絶対に必要（Must）」な要件と、「あれば望ましい（Want）」要件の区分け", "category": "思考法・フレームワーク" },
  { "term": "ブレスト", "meaning": "批判を禁止し、複数人で自由にアイデアを出し合う会議手法（ブレーンストーミング）", "category": "思考法・フレームワーク" },
  { "term": "4P分析", "meaning": "製品（Product）、価格（Price）、流通（Place）、販促（Promotion）の4要素からマーケティング戦略を立案する手法", "category": "思考法・フレームワーク" },
  { "term": "3C分析", "meaning": "市場・顧客（Customer）、競合（Competitor）、自社（Company）の3つの視点から環境分析を行う手法", "category": "思考法・フレームワーク" },
  { "term": "SWOT分析", "meaning": "自社の強み・弱みと、外部環境の機会・脅威の4要素を分析するフレームワーク", "category": "思考法・フレームワーク" },
  { "term": "ボトルネック", "meaning": "全体の処理能力や進行速度を制約している、最も能力の低い箇所や要因", "category": "思考法・フレームワーク" },
  { "term": "ゼロベース", "meaning": "過去の経緯や既存の枠組みにとらわれず、白紙の状態から考え直すこと", "category": "思考法・フレームワーク" },
  { "term": "ジャストアイデア", "meaning": "深い根拠や実現可能性の検討はまだ伴わない、単なる思いつきのアイデア", "category": "思考法・フレームワーク" },
  { "term": "PDCA", "meaning": "計画（Plan）、実行（Do）、評価（Check）、改善（Action）のサイクルを回し、業務を継続的に改善する手法", "category": "思考法・フレームワーク" },
  { "term": "バックエンド", "meaning": "Webシステムにおいて、サーバーやデータベースなど、ユーザーの目に見えない裏側の処理部分", "category": "IT・ツール" },
  { "term": "フロントエンド", "meaning": "Webシステムにおいて、ブラウザ上の画面表示や操作など、ユーザーの目に触れる部分", "category": "IT・ツール" },
  { "term": "CRM", "meaning": "顧客情報を一元管理し、顧客との関係性を維持・強化するためのシステムや手法（顧客関係管理）", "category": "IT・ツール" },
  { "term": "技術的負債", "meaning": "短期的な開発スピードを優先して書かれた「品質の低いコード」等が原因で、将来的に修正コストが増大すること", "category": "IT・ツール" },
  { "term": "リファクタリング", "meaning": "外部から見た振る舞いは変えずに、内部のプログラムコードを整理・改善すること", "category": "IT・ツール" },
  { "term": "デプロイ", "meaning": "開発したソフトウェアやシステムをサーバー等に配置し、利用可能な状態（本番公開）にすること", "category": "IT・ツール" },
  { "term": "レガシー", "meaning": "技術的に古くなり、保守や拡張が困難になったシステムや技術", "category": "IT・ツール" },
  { "term": "オンプレミス", "meaning": "自社施設内にサーバーなどの情報システム機器を設置・運用する形態", "category": "IT・ツール" },
  { "term": "LLM", "meaning": "大量のテキストデータを学習し、人間のような文章生成や理解を行うAIモデル（大規模言語モデル）", "category": "IT・ツール" },
  { "term": "プロンプトエンジニアリング", "meaning": "AIモデルから望ましい出力を得るために、入力する指示文（プロンプト）を最適化する技術", "category": "IT・ツール" },
  { "term": "ハルシネーション", "meaning": "生成AIが、事実に基づかない嘘の情報をもっともらしく生成してしまう現象（幻覚）", "category": "IT・ツール" },
  { "term": "アジャイル", "meaning": "短いサイクルで「計画→設計→実装→テスト」を繰り返し、柔軟にシステムを開発する手法", "category": "IT・ツール" },
  { "term": "API", "meaning": "異なるソフトウェアやアプリケーション同士がデータや機能をやり取りするための接続口", "category": "IT・ツール" },
  { "term": "DX", "meaning": "デジタル技術を活用して、ビジネスモデルや組織、企業文化を変革すること", "category": "IT・ツール" },
  { "term": "SaaS", "meaning": "ソフトウェアをインストールせず、インターネット経由でサービスとして利用する提供形態", "category": "IT・ツール" },
  { "term": "UI", "meaning": "ユーザーがシステムを利用する際の画面表示や操作方法などの接点（ユーザーインターフェース）", "category": "IT・ツール" },
  { "term": "ジェンスパ", "meaning": "AI検索エンジン・キュレーションツール「GenSpark」の略称", "category": "IT・ツール" },
  { "term": "スプシ", "meaning": "「Google スプレッドシート」の略称", "category": "IT・ツール" },
  { "term": "パイプライン", "meaning": "見込み顧客が契約に至るまでのプロセスや、現在進行中の案件一覧のこと", "category": "営業・CS" },
  { "term": "アウトバウンド", "meaning": "企業側から顧客に対してアプローチを行う、能動的な営業スタイル（テレアポなど）", "category": "営業・CS" },
  { "term": "インバウンド", "meaning": "顧客からの問い合わせや訪問を受け付ける、受動的な営業スタイル", "category": "営業・CS" },
  { "term": "クロージング", "meaning": "営業活動において、顧客に購入や契約の決断を促し、契約を締結する最終段階", "category": "営業・CS" },
  { "term": "オンボーディング", "meaning": "新規顧客や新入社員に対し、早期に定着・活躍できるようサポートするプロセス", "category": "営業・CS" },
  { "term": "クロスセル", "meaning": "商品を購入する顧客に対し、関連商品や別の商品を組み合わせて提案すること", "category": "営業・CS" },
  { "term": "アップセル", "meaning": "顧客に対し、検討中の商品より上位の高価なモデルを提案し、顧客単価を上げること", "category": "営業・CS" },
  { "term": "CS", "meaning": "顧客の成功体験を支援し、能動的にサポートすることでLTV最大化を目指す役割（カスタマーサクセス）", "category": "営業・CS" },
  { "term": "稟議設計", "meaning": "顧客担当者が社内でスムーズに決裁を得られるよう、営業側が決裁ルートや資料作成を支援すること", "category": "営業・CS" },
  { "term": "チャーンレート", "meaning": "顧客がサービスを解約したり、有料会員から退会したりする割合（解約率）", "category": "営業・CS" },
  { "term": "トップリード", "meaning": "成約の可能性が極めて高い、最重要の見込み顧客", "category": "営業・CS" },
  { "term": "BANT", "meaning": "法人営業で確認すべき4項目、予算(Budget)、決裁権(Authority)、ニーズ(Needs)、導入時期(Timeframe)の頭文字", "category": "営業・CS" },
  { "term": "トップアプローチ", "meaning": "現場の担当者ではなく、決裁権を持つ経営層や役員に直接営業を行うこと", "category": "営業・CS" },
  { "term": "フィールドセールス", "meaning": "顧客のもとへ訪問、または対面形式で商談を行い、契約獲得を目指す外勤営業", "category": "営業・CS" },
  { "term": "IS", "meaning": "電話やメール、Web会議などを活用し、非対面で営業活動を行う役割（インサイドセールス）", "category": "営業・CS" },
  { "term": "O2O", "meaning": "オンライン（Web）での活動を通じて、オフライン（実店舗）への送客を促すマーケティング施策", "category": "マーケティング" },
  { "term": "オムニチャネル", "meaning": "実店舗やネット、アプリなどあらゆる販売経路を統合し、どこでも同じように購入できる環境を作ること", "category": "マーケティング" },
  { "term": "A/Bテスト", "meaning": "2つのパターン（A案・B案）を用意して比較し、どちらの効果が高いかを検証する手法", "category": "マーケティング" },
  { "term": "バイラル", "meaning": "口コミやSNSでの共有を通じて、ウイルス感染のように情報が拡散していくこと", "category": "マーケティング" },
  { "term": "UGC", "meaning": "一般ユーザーによって制作・生成されたコンテンツ（SNSの投稿、レビュー、ブログなど）", "category": "マーケティング" },
  { "term": "インサイト", "meaning": "顧客自身も自覚していない、購買行動の裏にある隠れた動機や本音", "category": "マーケティング" },
  { "term": "ファネル", "meaning": "顧客が認知から購入に至る過程で、徐々に少数に絞り込まれていく様子を図式化したもの", "category": "マーケティング" },
  { "term": "リテンション", "meaning": "既存顧客との関係を維持し、継続的に利用してもらうための活動", "category": "マーケティング" },
  { "term": "ベネフィット", "meaning": "商品やサービスの機能ではなく、それを利用することで顧客が得られる「利益」や「嬉しい体験」", "category": "マーケティング" },
  { "term": "セグメント", "meaning": "市場や顧客を、年齢・性別・行動特性などの特定の基準で分類したグループ", "category": "マーケティング" },
  { "term": "ローンチ", "meaning": "新しい商品やサービスを市場に公開・発売すること", "category": "マーケティング" },
  { "term": "インプレッション", "meaning": "Web広告や投稿がユーザーの画面に表示された回数", "category": "マーケティング" },
  { "term": "CTA", "meaning": "Webサイト上で、ユーザーに具体的な行動（クリック、登録など）を促すためのボタンやリンク", "category": "マーケティング" },
  { "term": "CVR", "meaning": "Webサイトへの訪問者数のうち、購入や申込などの成果（コンバージョン）に至った割合", "category": "マーケティング" },
  { "term": "CTR", "meaning": "広告などが表示された回数のうち、実際にクリックされた割合（クリック率）", "category": "マーケティング" },
  { "term": "UX", "meaning": "ユーザーが製品やサービスを通じて得られる「体験」や「心地よさ」の総称", "category": "マーケティング" },
  { "term": "SEO", "meaning": "検索エンジンの検索結果で、Webサイトを上位に表示させるための最適化施策", "category": "マーケティング" },
  { "term": "MEO", "meaning": "地図アプリ（Googleマップ等）の検索結果で、店舗情報を上位に表示させるための施策", "category": "マーケティング" },
  { "term": "LTV", "meaning": "一人の顧客が取引開始から終了までに、企業にもたらす利益の総額（顧客生涯価値）", "category": "マーケティング" },
  { "term": "CV", "meaning": "Webサイトにおける最終的な成果（商品の購入、資料請求、会員登録など）のこと", "category": "マーケティング" },
  { "term": "リードナーチャリング", "meaning": "獲得した見込み顧客に対し、有益な情報提供などを行って購買意欲を高める活動（顧客育成）", "category": "マーケティング" },
  { "term": "LP", "meaning": "広告などを経由して最初に訪問する、購入や申込に特化したWebページ（ランディングページ）", "category": "マーケティング" },
  { "term": "ターゲット", "meaning": "自社の商品やサービスを売り込みたい対象となる顧客層", "category": "マーケティング" },
  { "term": "ペルソナ", "meaning": "自社のサービスを利用する典型的なユーザー像を、詳細な属性や心理まで定義した架空の人物モデル", "category": "マーケティング" },
  { "term": "MVV", "meaning": "企業の方向性を示すMission（使命）、Vision（あるべき姿）、Value（行動指針）の総称", "category": "経営・戦略" },
  { "term": "プラットフォーム", "meaning": "他社やユーザーが製品・サービスを提供したり交流したりするための「土台」や「基盤」となる環境", "category": "経営・戦略" },
  { "term": "コアコンピタンス", "meaning": "競合他社が真似できない、企業の中核となる独自の強みや能力", "category": "経営・戦略" },
  { "term": "フリーミアム", "meaning": "基本的なサービスを無料で提供し、高度な機能や特別なサービスを有料で提供するビジネスモデル", "category": "経営・戦略" },
  { "term": "サステナビリティ", "meaning": "環境・社会・経済の観点から、将来にわたって持続可能であること", "category": "経営・戦略" },
  { "term": "ゲームチェンジャー", "meaning": "既存の競争ルールや市場の枠組みを根底から変えてしまうような革新的な企業や製品", "category": "経営・戦略" },
  { "term": "パラダイムシフト", "meaning": "その時代に当然と考えられていた認識や価値観が、劇的に変化すること", "category": "経営・戦略" },
  { "term": "デファクトスタンダード", "meaning": "公的な規格ではないが、市場競争の結果として事実上の標準となったもの", "category": "経営・戦略" },
  { "term": "スキーム", "meaning": "目標を達成するための枠組みや、体系的な計画・仕組みのこと", "category": "経営・戦略" },
  { "term": "アセット", "meaning": "企業が保有する資産や財産。人材、ブランド、特許などの無形資産も含む", "category": "経営・戦略" },
  { "term": "カニバリ", "meaning": "自社の新商品が既存商品のシェアを奪ってしまう「共食い」現象のこと（カニバリゼーション）", "category": "経営・戦略" },
  { "term": "ピボット", "meaning": "スタートアップなどが、事業の方向性や路線を大きく転換・修正すること", "category": "経営・戦略" },
  { "term": "スケール", "meaning": "事業やシステムの規模を拡大すること", "category": "経営・戦略" },
  { "term": "マネタイズ", "meaning": "無料サービスや事業から収益を生み出す仕組みを作ること", "category": "経営・戦略" },
  { "term": "ブルーオーシャン", "meaning": "競争相手が存在しない、未開拓の市場領域のこと", "category": "経営・戦略" },
  { "term": "損益分岐点", "meaning": "売上高と費用が等しくなり、損益がゼロになる売上規模のこと（ブレークイーブンポイント）", "category": "経営・戦略" },
  { "term": "マージン", "meaning": "売上総利益（粗利）、または手数料や利ざやのこと。余裕幅を指すこともある", "category": "経営・戦略" },
  { "term": "キャッシュフロー", "meaning": "企業活動における現金の流れ（流入と流出）のこと", "category": "経営・戦略" },
  { "term": "BS", "meaning": "企業の一定時点における財政状態（資産・負債・純資産）を示す「貸借対照表」", "category": "経営・戦略" },
  { "term": "PL", "meaning": "企業の一定期間における経営成績（収益・費用・利益）を示す「損益計算書」", "category": "経営・戦略" },
  { "term": "MoM / YoY", "meaning": "前月比（Month over Month）および前年比（Year over Year）を表す略語", "category": "経営・戦略" },
  { "term": "シナジー", "meaning": "複数の要素が組み合わさることで、単体の総和以上の大きな効果を生むこと（相乗効果）", "category": "経営・戦略" },
  { "term": "CAC", "meaning": "顧客一人を獲得するために費やしたコスト（顧客獲得単価）", "category": "経営・戦略" },
  { "term": "ガバナンス", "meaning": "企業が公正な活動を行うために、自らを管理・統制する仕組み（コーポレートガバナンス）", "category": "経営・戦略" },
  { "term": "アライアンス", "meaning": "複数の企業が互いの利益のために提携・協力関係を結ぶこと", "category": "経営・戦略" },
  { "term": "ARR", "meaning": "毎年決まって得られる収益の年間合計額（年間経常収益）", "category": "経営・戦略" },
  { "term": "MRR", "meaning": "毎月決まって得られる収益の月間合計額（月次経常収益）", "category": "経営・戦略" },
  { "term": "ROI", "meaning": "投資した資本に対して、どれだけの利益が得られたかを示す指標（投資対効果）", "category": "経営・戦略" },
  { "term": "カーブアウト", "meaning": "企業が事業の一部を切り出し、外部資本などを入れて独立した会社として設立すること", "category": "経営・戦略" },
  { "term": "スピンオフ", "meaning": "企業が特定の一部門を切り離し、親子関係や資本関係を保ったまま独立させること", "category": "経営・戦略" },
  { "term": "FS", "meaning": "新規事業やプロジェクトの実現可能性を事前に調査・検証すること（フィージビリティスタディ）", "category": "経営・戦略" },
  { "term": "KPI", "meaning": "最終目標を達成するための過程における、重要な中間指標（重要業績評価指標）", "category": "経営・戦略" },
  { "term": "PoC", "meaning": "新しいアイデアや技術が実現可能かどうかを簡易的に検証すること（概念実証）", "category": "経営・戦略" },
  { "term": "KGI", "meaning": "企業やプロジェクトが達成すべき最終的な定量目標（重要目標達成指標）", "category": "経営・戦略" }
]

# -----------------------------------------------------------------------------
# Configuration & Styling
# -----------------------------------------------------------------------------

st.set_page_config(
    page_title="BizTerm Master",
    page_icon="🏆",
    layout="centered"
)

# Custom CSS to match the previous design feel
st.markdown("""
<style>
    .stButton > button {
        width: 100%;
        border-radius: 12px;
        padding: 0.5rem 1rem;
        font-weight: 600;
        background-color: #f3f4f6;
        color: #1f2937;
        border: 1px solid #e5e7eb;
        transition: all 0.2s;
    }
    .stButton > button:hover {
        background-color: #e0e7ff;
        border-color: #c7d2fe;
        color: #4338ca;
    }
    .stProgress > div > div > div > div {
        background-color: #4f46e5;
    }
    .category-tag {
        background-color: #e0e7ff;
        color: #4338ca;
        padding: 0.2rem 0.6rem;
        border-radius: 9999px;
        font-size: 0.75rem;
        font-weight: 600;
        display: inline-block;
        margin-bottom: 0.5rem;
    }
    .card-container {
        background-color: white;
        color: #1f2937; /* Force dark text color for readability in dark mode */
        padding: 2rem;
        border-radius: 1rem;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
        margin-bottom: 2rem;
    }
    .result-correct {
        border-left: 4px solid #22c55e;
        background-color: #f0fdf4;
        color: #1f2937; /* Force dark text */
        padding: 1rem;
        border-radius: 0.5rem;
        margin-bottom: 1rem;
    }
    .result-wrong {
        border-left: 4px solid #ef4444;
        background-color: #fef2f2;
        color: #1f2937; /* Force dark text */
        padding: 1rem;
        border-radius: 0.5rem;
        margin-bottom: 1rem;
    }
</style>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# State Management
# -----------------------------------------------------------------------------

if 'game_state' not in st.session_state:
    st.session_state.game_state = 'MENU' # MENU, PLAYING, FEEDBACK, RESULT
if 'questions' not in st.session_state:
    st.session_state.questions = []
if 'current_index' not in st.session_state:
    st.session_state.current_index = 0
if 'results' not in st.session_state:
    st.session_state.results = []
if 'last_selected_option' not in st.session_state:
    st.session_state.last_selected_option = None
if 'last_is_correct' not in st.session_state:
    st.session_state.last_is_correct = False

# -----------------------------------------------------------------------------
# Helper Functions
# -----------------------------------------------------------------------------

def start_game(num_questions):
    pool = VOCABULARY_LIST.copy()
    random.shuffle(pool)
    selected_items = pool[:num_questions]
    
    generated_questions = []
    for item in selected_items:
        others = [t["term"] for t in VOCABULARY_LIST if t["term"] != item["term"]]
        distractors = random.sample(others, 3)
        options = distractors + [item["term"]]
        random.shuffle(options)
        
        generated_questions.append({
            "term": item["term"],
            "meaning": item["meaning"],
            "category": item["category"],
            "options": options
        })
    
    st.session_state.questions = generated_questions
    st.session_state.current_index = 0
    st.session_state.results = []
    st.session_state.game_state = 'PLAYING'

def check_answer(selected_option):
    current_q = st.session_state.questions[st.session_state.current_index]
    is_correct = (selected_option == current_q['term'])
    
    st.session_state.results.append({
        "question": current_q,
        "selected": selected_option,
        "is_correct": is_correct
    })
    
    st.session_state.last_selected_option = selected_option
    st.session_state.last_is_correct = is_correct
    st.session_state.game_state = 'FEEDBACK'

def next_question():
    if st.session_state.current_index < len(st.session_state.questions) - 1:
        st.session_state.current_index += 1
        st.session_state.game_state = 'PLAYING'
    else:
        st.session_state.game_state = 'RESULT'

def restart_game():
    st.session_state.game_state = 'MENU'
    st.session_state.questions = []
    st.session_state.results = []

# -----------------------------------------------------------------------------
# UI Renderers
# -----------------------------------------------------------------------------

def show_start_screen():
    st.markdown("<div style='text-align: center; padding: 2rem;'>", unsafe_allow_html=True)
    st.title("BizTerm Master")
    st.caption("ビジネス用語・IT用語の理解度をテストしましょう。")
    st.markdown("</div>", unsafe_allow_html=True)

    with st.container():
        st.write("")
        st.markdown("### 問題設定")
        num_questions = st.slider("問題数を選択してください", min_value=5, max_value=len(VOCABULARY_LIST), value=10)
        
        st.write("")
        if st.button("テストを開始する", type="primary", use_container_width=True):
            start_game(num_questions)
            st.rerun()

def show_quiz_screen():
    current_q = st.session_state.questions[st.session_state.current_index]
    total = len(st.session_state.questions)
    current = st.session_state.current_index + 1
    progress = st.session_state.current_index / total

    st.progress(progress)
    
    col1, col2 = st.columns([1, 1])
    with col1:
        st.markdown(f"**Question {current}** / {total}")
    with col2:
        st.markdown(f"<div style='text-align: right;'><span class='category-tag'>{current_q['category']}</span></div>", unsafe_allow_html=True)

    st.markdown(f"""
    <div class="card-container">
        <h3 style="margin-top:0;">{current_q['meaning']}</h3>
    </div>
    """, unsafe_allow_html=True)

    # Options Grid
    options = current_q['options']
    
    # We use columns to create a grid layout for buttons
    # In Streamlit, buttons trigger a rerun. We use a callback or just standard flow.
    for option in options:
        if st.button(option, key=option, use_container_width=True):
            check_answer(option)
            st.rerun()

def show_feedback_screen():
    # Show the same question info but with result
    current_q = st.session_state.questions[st.session_state.current_index]
    selected = st.session_state.last_selected_option
    is_correct = st.session_state.last_is_correct
    
    st.progress((st.session_state.current_index + 1) / len(st.session_state.questions))
    
    if is_correct:
        st.success(f"正解！ ({current_q['term']})")
    else:
        st.error(f"不正解... 正解は「{current_q['term']}」でした。")
        st.markdown(f"あなたの回答: **{selected}**")

    st.markdown(f"""
    <div class="card-container">
        <div style="color: #6b7280; font-size: 0.9rem; margin-bottom: 0.5rem;">{current_q['category']}</div>
        <h3 style="margin-top:0;">{current_q['meaning']}</h3>
    </div>
    """, unsafe_allow_html=True)

    if st.button("次の問題へ" if st.session_state.current_index < len(st.session_state.questions) - 1 else "結果を見る", type="primary", use_container_width=True):
        next_question()
        st.rerun()

def show_result_screen():
    results = st.session_state.results
    correct_count = len([r for r in results if r['is_correct']])
    total = len(results)
    percentage = int((correct_count / total) * 100)
    
    st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
    st.title("結果発表")
    st.markdown(f"<h1 style='font-size: 4rem; margin: 0;'>{percentage}%</h1>", unsafe_allow_html=True)
    st.write(f"{total}問中 {correct_count}問正解")
    
    msg = ""
    if percentage == 100: msg = "完璧です！素晴らしい！ 🏆"
    elif percentage >= 80: msg = "すごい！高得点です！ 🎉"
    elif percentage >= 60: msg = "その調子！あと少しです。 👍"
    else: msg = "次はもっと頑張ろう！ 💪"
    st.markdown(f"### {msg}")
    st.markdown("</div>", unsafe_allow_html=True)
    
    if st.button("もう一度挑戦する", type="primary", use_container_width=True):
        restart_game()
        st.rerun()
    
    st.divider()
    st.subheader("振り返り")
    
    for i, r in enumerate(results):
        q = r['question']
        is_correct = r['is_correct']
        css_class = "result-correct" if is_correct else "result-wrong"
        icon = "✅" if is_correct else "❌"
        
        # Prepare optional HTML for incorrect answers
        your_answer_html = ""
        if not is_correct:
            your_answer_html = f'<div><span style="color: #6b7280;">あなたの回答:</span> <span style="font-weight: bold; color: #b91c1c; text-decoration: line-through;">{r["selected"]}</span></div>'

        # Use textwrap.dedent or just remove indentation to avoid Markdown code block formatting
        st.markdown(f"""
<div class="{css_class}">
<div style="font-size: 0.8rem; font-weight: bold; color: #6b7280;">Q.{i+1} {q['category']} {icon}</div>
<div style="font-weight: 500; margin: 0.5rem 0;">{q['meaning']}</div>
<div style="display: flex; gap: 1rem; font-size: 0.9rem;">
<div>
<span style="color: #6b7280;">正解:</span>
<span style="font-weight: bold; color: #15803d;">{q['term']}</span>
</div>
{your_answer_html}
</div>
</div>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# Main Routing
# -----------------------------------------------------------------------------

def main():
    if st.session_state.game_state == 'MENU':
        show_start_screen()
    elif st.session_state.game_state == 'PLAYING':
        show_quiz_screen()
    elif st.session_state.game_state == 'FEEDBACK':
        show_feedback_screen()
    elif st.session_state.game_state == 'RESULT':
        show_result_screen()

if __name__ == "__main__":
    main()
