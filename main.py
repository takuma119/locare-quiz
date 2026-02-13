import random
from js import document, console, window
from pyodide.ffi import create_proxy

# Vocabulary List
VOCABULARY_LIST = [
  { "term": "スコープ", "meaning": "範囲、対象領域。「それは今回のプロジェクトのスコープ外です（対象外なのでやりません）」", "category": "ビジネス基礎" },
  { "term": "カンバン", "meaning": "タスクを「未着手」「進行中」「完了」などのボードに貼り付けて管理する手法。トヨタ生産方式が発祥", "category": "ビジネス基礎" },
  { "term": "ガントチャート", "meaning": "プロジェクトのスケジュール管理表。横軸に時間、縦軸に作業項目をとり、進捗を棒グラフで可視化したもの", "category": "ビジネス基礎" },
  { "term": "クリティカルパス", "meaning": "プロジェクトの中で、ここが遅れると全体の納期が遅れてしまう「最重要の作業経路」のこと", "category": "ビジネス基礎" },
  { "term": "リードタイム", "meaning": "発注から納品まで、または作業開始から完了までにかかる所要時間", "category": "ビジネス基礎" },
  { "term": "たたき台", "meaning": "議論や検討を始めるための、とりあえずの試案・原案。「完成度は低くていいからたたき台作って」", "category": "ビジネス基礎" },
  { "term": "FB", "meaning": "Feedback（フィードバック）。成果物に対する評価や改善点の指摘。「資料のFBお願いします」", "category": "ビジネス基礎" },
  { "term": "ASAP", "meaning": "As Soon As Possible（なる早で）。「アサップ」と読む。「これASAPでお願いします」", "category": "ビジネス基礎" },
  { "term": "MTG", "meaning": "Meeting（ミーティング）の略称。チャットやカレンダーで多用される", "category": "ビジネス基礎" },
  { "term": "TBD", "meaning": "To Be Determined（未定）。資料などで、まだ決まっていない数値や日付の箇所に仮置きしておく記号", "category": "ビジネス基礎" },
  { "term": "アンラーニング", "meaning": "学習棄却。過去の成功体験や古い知識を意識的に捨てて、新しい環境に適応するために学び直すこと", "category": "ビジネス基礎" },
  { "term": "プロパー", "meaning": "本来の、正規の。文脈によるが、「新卒からの生え抜き社員」や「正社員（派遣や委託に対して）」を指すことが多い", "category": "ビジネス基礎" },
  { "term": "ブラックボックス", "meaning": "中身の仕組みが複雑すぎて、どうなっているか分からない状態のこと。「あの業務は属人化してブラックボックス化している」", "category": "ビジネス基礎" },
  { "term": "コンフリクト", "meaning": "衝突、対立。意見が食い違ったり、利害が対立している状態。「スケジュールのコンフリクト（バッティング）」としても使う", "category": "ビジネス基礎" },
  { "term": "ハレーション", "meaning": "元々は写真用語（光が強すぎて白飛びすること）。ビジネスでは「周囲への悪影響」や「強い反発」を意味する。「これをやると他部署とハレーションが起きる」", "category": "ビジネス基礎" },
  { "term": "キックオフ", "meaning": "プロジェクトの開始、決起集会。「キックオフミーティング」でメンバーの顔合わせと目標共有を行う", "category": "ビジネス基礎" },
  { "term": "フェーズ", "meaning": "段階、局面。プロジェクトの進捗を「フェーズ1」「フェーズ2」と区切って管理するときに使う", "category": "ビジネス基礎" },
  { "term": "イニシアチブ", "meaning": "主導権。「イニシアチブを取る（＝自分たちがリードして進める）」のように使う", "category": "ビジネス基礎" },
  { "term": "キャッチアップ", "meaning": "遅れを取り戻すこと、または未経験の分野を急いで勉強して追いつくこと", "category": "ビジネス基礎" },
  { "term": "バジェット", "meaning": "予算のこと。「今期はバジェットが足りない」のように使う", "category": "ビジネス基礎" },
  { "term": "マター", "meaning": "担当、責任の所在。「これは営業部マター（営業部の責任範囲）です」のように使う", "category": "ビジネス基礎" },
  { "term": "オンスケ", "meaning": "オンスケジュールの略。作業が計画通り（遅れずに）進んでいること。「進捗はオンスケです」", "category": "ビジネス基礎" },
  { "term": "リスケ", "meaning": "リスケジュールの略。予定の日時を変更すること。「来週にリスケお願いできますか？」", "category": "ビジネス基礎" },
  { "term": "ペンディング", "meaning": "保留、先送りにすること。中止ではなく「一旦置いておく」ニュアンスで使う", "category": "ビジネス基礎" },
  { "term": "フィックス", "meaning": "決定する、確定すること。「仕様をフィックスさせる」「スケジュールがフィックスした」", "category": "ビジネス基礎" },
  { "term": "アサイン", "meaning": "担当者を任命すること。「次のプロジェクトに田中さんをアサインする」のように使う", "category": "ビジネス基礎" },
  { "term": "エビデンス", "meaning": "証拠、言質。「エビデンスはあるの？」と、提案の根拠となるデータや議事録を求めるときに使う", "category": "ビジネス基礎" },
  { "term": "心理的安全性", "meaning": "チーム内で「何を言っても罰せられない、拒絶されない」という安心感のこと。これが高いと生産性が上がるとされる", "category": "ビジネス基礎" },
  { "term": "キャパシティ", "meaning": "許容範囲、能力の限界。「キャパ」と略される。「キャパオーバー（仕事量が限界を超えた）」のように使う", "category": "ビジネス基礎" },
  { "term": "エンゲージメント", "meaning": "会社や組織に対する「愛着心」や「貢献意欲」のこと。これが高い社員ほど離職率が低く、パフォーマンスが高いとされる", "category": "ビジネス基礎" },
  { "term": "OJT", "meaning": "On-the-Job Training。実際の業務をやりながら、先輩や上司が仕事を教える教育手法", "category": "ビジネス基礎" },
  { "term": "リスクヘッジ", "meaning": "起こりうるリスクを予測して、あらかじめ回避策や備えを用意しておくこと", "category": "ビジネス基礎" },
  { "term": "ブラッシュアップ", "meaning": "企画書や資料、アイデアなどを磨き上げて、より良くすること", "category": "ビジネス基礎" },
  { "term": "ベストプラクティス", "meaning": "最も効率的で効果的な手法、成功事例のこと。「過去のベストプラクティスを参考にする」のように使う", "category": "ビジネス基礎" },
  { "term": "ナレッジ", "meaning": "企業や個人が持っている「知識・経験・ノウハウ」のこと。「ナレッジを共有する」のように使う", "category": "ビジネス基礎" },
  { "term": "工数", "meaning": "作業にかかる時間や手間の量。「人月（1人が1ヶ月かかる量）」や「人日」という単位で表す", "category": "ビジネス基礎" },
  { "term": "1on1", "meaning": "上司と部下が定期的に行う1対1のミーティング。評価面談ではなく、部下の成長支援や悩み相談が目的", "category": "ビジネス基礎" },
  { "term": "NDA", "meaning": "Non-Disclosure Agreement（秘密保持契約）。取引前に「情報を漏らしません」と約束する契約書のこと", "category": "ビジネス基礎" },
  { "term": "エスカレーション", "meaning": "上司や上位の担当者に報告・相談して、対応や判断を仰ぐこと。トラブルが起きた時に「エスカレする」と言う", "category": "ビジネス基礎" },
  { "term": "コミット", "meaning": "Commitment（約束、委任）。ビジネスでは「結果を約束する」「責任を持ってやり遂げる」という意味で使われる（例：数字にコミットする）", "category": "ビジネス基礎" },
  { "term": "インセンティブ", "meaning": "意欲を引き出すための「動機付け」や「報奨金」のこと。営業成績に応じたボーナスなどを指すことが多い", "category": "ビジネス基礎" },
  { "term": "コンセンサス", "meaning": "「合意」のこと。関係者全員の意見が一致している状態。「ネゴ（根回し）」の結果として得るもの", "category": "ビジネス基礎" },
  { "term": "コンプライアンス", "meaning": "法令遵守。法律だけでなく、社会的な規範や倫理観を守って活動すること", "category": "ビジネス基礎" },
  { "term": "リソース", "meaning": "資源のこと。ビジネスでは主に「人（人員）」「時間」「予算」の3つを指す", "category": "ビジネス基礎" },
  { "term": "バッファ", "meaning": "予備、余裕のこと。スケジュールや予算において、不測の事態に備えて確保しておく余白", "category": "ビジネス基礎" },
  { "term": "アジェンダ", "meaning": "会議における議題や検討事項のリスト。または行動計画のこと", "category": "ビジネス基礎" },
  { "term": "B2C", "meaning": "Business to Consumer。企業が「一般消費者」に対してモノやサービスを売るビジネス", "category": "ビジネス基礎" },
  { "term": "ステークホルダー", "meaning": "利害関係者。株主、経営者、従業員、顧客、取引先など、そのプロジェクトや企業活動に関わるすべての人", "category": "ビジネス基礎" },
  { "term": "B2B", "meaning": "Business to Business。企業が「企業」に対してモノやサービスを売るビジネス", "category": "ビジネス基礎" },
  { "term": "マイルストーン", "meaning": "プロジェクトの長期スケジュールの中で設ける、重要な節目や中間チェックポイント", "category": "ビジネス基礎" },
  { "term": "エンプラ", "meaning": "エンタープライズの略で、大企業のこと", "category": "ビジネス基礎" },
  { "term": "SMB", "meaning": "中堅・中小企業（Small to Medium Business）のこと", "category": "ビジネス基礎" },
  { "term": "仮説思考", "meaning": "情報が全て揃うのを待たず、「たぶんこうだろう」という仮の結論（仮説）を先に持ち、それを検証しながら進める思考法", "category": "思考法・フレームワーク" },
  { "term": "粒度", "meaning": "グレニュラリティ。物事の細かさのレベル。「話の粒度を合わせよう（詳細レベルの話なのか、全体像の話なのか）」", "category": "思考法・フレームワーク" },
  { "term": "マスト / ウォント", "meaning": "Must（絶対に必要な要件）とWant（あったらいいな程度の要件）。システム開発や採用条件の優先順位付けで使う", "category": "思考法・フレームワーク" },
  { "term": "ブレスト", "meaning": "ブレーンストーミングの略。批判禁止で、自由な発想でアイデアを出し合う会議のこと", "category": "思考法・フレームワーク" },
  { "term": "4P分析", "meaning": "Product（製品）、Price（価格）、Place（流通）、Promotion（販促）の4要素でマーケティング戦略を考えるフレームワーク", "category": "思考法・フレームワーク" },
  { "term": "3C分析", "meaning": "Customer（市場・顧客）、Competitor（競合）、Company（自社）の3視点で戦略を練るフレームワーク", "category": "思考法・フレームワーク" },
  { "term": "SWOT分析", "meaning": "強み（Strength）、弱み（Weakness）、機会（Opportunity）、脅威（Threat）の4視点で現状を分析するフレームワーク", "category": "思考法・フレームワーク" },
  { "term": "ボトルネック", "meaning": "業務フローやシステムの中で、全体の処理速度や成果を落としている「詰まり」や「一番弱い部分」のこと", "category": "思考法・フレームワーク" },
  { "term": "ゼロベース", "meaning": "過去の経緯や「こうあるべき」という既成概念を捨てて、白紙の状態から考え直すこと", "category": "思考法・フレームワーク" },
  { "term": "ジャストアイデア", "meaning": "根拠や実現性は一旦置いておいて、ふと思いついたアイデアのこと", "category": "思考法・フレームワーク" },
  { "term": "PDCA", "meaning": "Plan（計画）、Do（実行）、Check（評価）、Action（改善）の4段階を繰り返し、業務を継続的に改善するフレームワーク", "category": "思考法・フレームワーク" },
  { "term": "バックエンド", "meaning": "ユーザーの目に見えない、サーバー側やデータベースの処理を行うシステム部分（Java, Python, PHPなど）", "category": "IT・ツール" },
  { "term": "フロントエンド", "meaning": "ユーザーの目に触れる、Webサイトやアプリの画面表示・操作部分（HTML, CSS, JavaScriptなど）", "category": "IT・ツール" },
  { "term": "CRM", "meaning": "Customer Relationship Management（顧客関係管理）。顧客情報を一元管理し、関係性を強化するシステム（例：Salesforce）", "category": "IT・ツール" },
  { "term": "技術的負債", "meaning": "開発スピードを優先して「汚いコード」を書いた結果、後になって修正が大変になること。「借金」に見立ててこう呼ぶ", "category": "IT・ツール" },
  { "term": "リファクタリング", "meaning": "プログラムの挙動は変えずに、内部のコードを整理してきれいにすること。将来のバグを防ぐために重要", "category": "IT・ツール" },
  { "term": "デプロイ", "meaning": "開発したシステムやプログラムを、実際にサーバーに配置して利用可能な状態（本番公開）にすること", "category": "IT・ツール" },
  { "term": "レガシー", "meaning": "過去の遺産。ITでは「古くなって使いにくいシステム（技術的負債）」という悪い意味で使われることが多い", "category": "IT・ツール" },
  { "term": "オンプレミス", "meaning": "オンプレ。自社の中にサーバーなどの設備を置いて運用すること。クラウド（SaaSなど）の対義語", "category": "IT・ツール" },
  { "term": "LLM", "meaning": "Large Language Model（大規模言語モデル）。膨大なテキストデータを学習し、人間のような文章を生成できるAIモデル（GPT-4など）", "category": "IT・ツール" },
  { "term": "プロンプトエンジニアリング", "meaning": "AI（ChatGPTなど）に対して、より適切な回答を引き出すために、指示文（プロンプト）を工夫・最適化する技術", "category": "IT・ツール" },
  { "term": "ハルシネーション", "meaning": "Hallucination（幻覚）。AIが事実とは異なる嘘の情報を、あたかも正しいかのように生成してしまう現象のこと", "category": "IT・ツール" },
  { "term": "アジャイル", "meaning": "「素早い」という意味。計画を細かく区切り、少しずつ作っては修正を繰り返す、柔軟なシステム開発手法", "category": "IT・ツール" },
  { "term": "API", "meaning": "Application Programming Interface。異なるソフトウェアやアプリ同士をつなぐ「接続口」のこと（例：スプシとSalesforceをAPIで連携する）", "category": "IT・ツール" },
  { "term": "DX", "meaning": "デジタルトランスフォーメーション。単にIT化するだけでなく、デジタル技術を使ってビジネスモデルや企業文化そのものを変革すること", "category": "IT・ツール" },
  { "term": "SaaS", "meaning": "Software as a Service（サース）。ソフトウェアをインストールせず、クラウド経由で利用するサービス形態（例：Salesforce, Slack, Zoom）", "category": "IT・ツール" },
  { "term": "UI", "meaning": "ユーザーインターフェース。Webサイトやアプリの見た目、操作画面、レイアウトのこと", "category": "IT・ツール" },
  { "term": "ジェンスパ", "meaning": "AIツールのgensparkの略称", "category": "IT・ツール" },
  { "term": "スプシ", "meaning": "Google スプレッドシートの略称", "category": "IT・ツール" },
  { "term": "パイプライン", "meaning": "初回接触から契約までの、現在進行中の「案件一覧」のこと。営業の見込み案件を可視化したもの", "category": "営業・CS" },
  { "term": "アウトバウンド", "meaning": "テレアポや飛び込み営業など、企業側から顧客にアプローチする「攻め」の営業スタイル", "category": "営業・CS" },
  { "term": "インバウンド", "meaning": "顧客からの問い合わせや来店を待つ「受け身」の営業スタイル（Webマーケティングなど）", "category": "営業・CS" },
  { "term": "クロージング", "meaning": "営業活動の最終段階。顧客に契約の決断を迫り、契約書にサインをもらうこと", "category": "営業・CS" },
  { "term": "オンボーディング", "meaning": "新規顧客や新入社員に対して、サービスや組織に定着し、早期に活躍できるようにサポートするプロセス", "category": "営業・CS" },
  { "term": "クロスセル", "meaning": "商品を購入する顧客に、関連商品やオプションをセットで提案して購入してもらうこと", "category": "営業・CS" },
  { "term": "アップセル", "meaning": "既存の顧客に、より上位のプランや高価な商品を提案して、顧客単価を上げること", "category": "営業・CS" },
  { "term": "CS", "meaning": "カスタマーサクセス。契約後の顧客に対して能動的に関わり、サービスの活用支援や成功体験を作ることで解約を防ぐ役割", "category": "営業・CS" },
  { "term": "稟議設計", "meaning": "顧客の担当者が社内でスムーズに決裁をとれるように、営業マンが資料作成や根回しのシナリオを一緒に作ってあげること", "category": "営業・CS" },
  { "term": "チャーンレート", "meaning": "解約率。サブスクリプション型ビジネスなどで、顧客がサービスを辞めてしまう割合のこと", "category": "営業・CS" },
  { "term": "トップリード", "meaning": "トップアプローチでつながった相手、または成約の可能性が非常に高い重要な見込み顧客", "category": "営業・CS" },
  { "term": "BANT", "meaning": "Budget（予算）、Authority（決裁権）、Needs（必要性）、Timeframe（時期）の頭文字。法人営業で必ず確認すべき4項目", "category": "営業・CS" },
  { "term": "トップアプローチ", "meaning": "現場ではなく、決裁権を持つ社長や役員クラスに直接営業をかける手法", "category": "営業・CS" },
  { "term": "フィールドセールス", "meaning": "顧客のもとへ訪問、またはWeb会議で対面して商談を行い、契約を勝ち取る外勤営業", "category": "営業・CS" },
  { "term": "IS", "meaning": "インサイドセールス。電話やメール、Zoomなどを使い、非対面で見込み顧客と関係を構築する内勤営業", "category": "営業・CS" },
  { "term": "O2O", "meaning": "Online to Offline。ネット（Online）で集客し、実店舗（Offline）への来店を促す施策のこと（クーポンの配布など）", "category": "マーケティング" },
  { "term": "オムニチャネル", "meaning": "実店舗、ネット通販、アプリなど、あらゆる販売経路を連携させ、どこでも同じように購入できる環境を作ること", "category": "マーケティング" },
  { "term": "A/Bテスト", "meaning": "Webサイトや広告で、A案とB案の2パターンを用意し、どちらの効果が高いかを実際にユーザーに見せて検証する手法", "category": "マーケティング" },
  { "term": "バイラル", "meaning": "「ウイルス性の」という意味。口コミやSNSでの拡散によって、商品やサービスが爆発的に広まること", "category": "マーケティング" },
  { "term": "UGC", "meaning": "User Generated Content。一般ユーザーによって作られたコンテンツ（SNSの口コミ、ブログ、動画など）。広告よりも信頼されやすい", "category": "マーケティング" },
  { "term": "インサイト", "meaning": "顧客自身も気づいていない、購買行動の奥底にある「隠れた本音・動機」のこと", "category": "マーケティング" },
  { "term": "ファネル", "meaning": "漏斗（じょうご）。顧客が認知→検討→購入へと進むにつれて数が減っていく様子を図式化したもの", "category": "マーケティング" },
  { "term": "リテンション", "meaning": "既存顧客の維持、引き留め。チャーン（解約）を防ぐための施策全般を指す", "category": "マーケティング" },
  { "term": "ベネフィット", "meaning": "商品そのものの機能（メリット）ではなく、それを使うことで顧客が得られる「嬉しい未来・体験」のこと", "category": "マーケティング" },
  { "term": "セグメント", "meaning": "市場や顧客を特定の条件（年齢、地域、行動など）で分けた「区分」のこと", "category": "マーケティング" },
  { "term": "ローンチ", "meaning": "新しいサービスや商品を世の中に公開・発売すること", "category": "マーケティング" },
  { "term": "インプレッション", "meaning": "広告や投稿が表示された回数のこと（Impと略される）。クリックされる（CTR）前の母数として重要", "category": "マーケティング" },
  { "term": "CTA", "meaning": "Call to Action（行動喚起）。Webサイト上で、ユーザーに具体的な行動（クリックや登録）を促すボタンやリンクのこと", "category": "マーケティング" },
  { "term": "CVR", "meaning": "Conversion Rate（コンバージョン率）。サイト訪問者のうち、購入や申込に至った割合", "category": "マーケティング" },
  { "term": "CTR", "meaning": "Click Through Rate（クリック率）。表示された回数のうち、実際にクリックされた割合", "category": "マーケティング" },
  { "term": "UX", "meaning": "ユーザーエクスペリエンス。サービスを通じてユーザーが得られる「体験」や「心地よさ」のこと", "category": "マーケティング" },
  { "term": "SEO", "meaning": "検索エンジン最適化。Googleなどの検索結果で、自分のWebサイトを上位に表示させるための対策", "category": "マーケティング" },
  { "term": "MEO", "meaning": "マップエンジン最適化。Googleマップなどの地図検索で、自分のお店を上位に表示させる対策", "category": "マーケティング" },
  { "term": "LTV", "meaning": "顧客生涯価値。一人の顧客が、取引開始から終了までに企業にもたらす利益の総額", "category": "マーケティング" },
  { "term": "CV", "meaning": "コンバージョン。Webサイト訪問者が、購入や資料請求など、そのサイトの「目標」となる行動を起こすこと", "category": "マーケティング" },
  { "term": "リードナーチャリング", "meaning": "獲得した見込み顧客（リード）に対して、有益な情報提供などを続け、購買意欲を高めていく（育成する）活動のこと", "category": "マーケティング" },
  { "term": "LP", "meaning": "ランディングページ。広告などをクリックした先に表示される、商品の購入や申込みに特化した縦長のWebページ", "category": "マーケティング" },
  { "term": "ターゲット", "meaning": "見込み顧客を属性（30代、男性、会社員など）でグループ分けした集団のこと", "category": "マーケティング" },
  { "term": "ペルソナ", "meaning": "サービスを利用する「たった一人の架空の人物像」。氏名、年齢、趣味、悩みなどを細かく設定したもの", "category": "マーケティング" },
  { "term": "MVV", "meaning": "Mission（使命）、Vision（将来像）、Value（行動指針）。企業の存在意義や方向性を定めたもの", "category": "経営・戦略" },
  { "term": "プラットフォーム", "meaning": "土台、基盤。AmazonやApp Storeのように、他社やユーザーが活動するための「場」を提供するビジネスモデル", "category": "経営・戦略" },
  { "term": "コアコンピタンス", "meaning": "他社には真似できない、その企業の中核となる強みや技術力のこと", "category": "経営・戦略" },
  { "term": "フリーミアム", "meaning": "基本的なサービスは無料で提供し、高度な機能や追加オプションを有料（プレミアム）にするビジネスモデル", "category": "経営・戦略" },
  { "term": "サステナビリティ", "meaning": "持続可能性。環境・社会・経済の3つの観点から、将来にわたって事業を継続できる状態を目指す考え方", "category": "経営・戦略" },
  { "term": "ゲームチェンジャー", "meaning": "既存の競争ルールや市場の常識を根底から覆してしまうような、革新的な製品や企業のこと（例：iPhone、Uber）", "category": "経営・戦略" },
  { "term": "パラダイムシフト", "meaning": "その時代の当たり前だった価値観や常識が、劇的に変化すること（例：天動説→地動説、ガラケー→スマホ）", "category": "経営・戦略" },
  { "term": "デファクトスタンダード", "meaning": "「事実上の標準」。公的な規格ではないが、シェアが高すぎて業界標準になってしまったもの（例：Windows、Microsoft Office）", "category": "経営・戦略" },
  { "term": "スキーム", "meaning": "枠組み、計画の仕組み。「新しい販売スキームを構築する」のように、単なる計画よりも「仕組み」のニュアンスが強い", "category": "経営・戦略" },
  { "term": "アセット", "meaning": "資産、強み。お金だけでなく、人材、ブランド、特許、顧客リストなど、企業が持つ「武器」のこと", "category": "経営・戦略" },
  { "term": "カニバリ", "meaning": "カニバリゼーション（共食い）。自社の新商品が、既存商品の売上を奪ってしまう現象のこと", "category": "経営・戦略" },
  { "term": "ピボット", "meaning": "方向転換。スタートアップなどが、当初の事業計画がうまくいかず、路線を変更すること", "category": "経営・戦略" },
  { "term": "スケール", "meaning": "事業規模を拡大すること。「このビジネスモデルはスケールしやすい（拡大しやすい）」のように使う", "category": "経営・戦略" },
  { "term": "マネタイズ", "meaning": "収益化。無料サービスや集めたアクセスを、どうやってお金に変えるかという仕組みのこと", "category": "経営・戦略" },
  { "term": "ブルーオーシャン", "meaning": "競争相手がいない未開拓の市場のこと。反対に、競合が激しく血で血を洗う市場を「レッドオーシャン」と呼ぶ", "category": "経営・戦略" },
  { "term": "損益分岐点", "meaning": "売上と費用がちょうど同じになり、利益がゼロ（赤字でも黒字でもない）になる地点のこと。これを超えると利益が出始める", "category": "経営・戦略" },
  { "term": "マージン", "meaning": "利益、利ざやのこと。または「余白・余裕」の意味でも使われる", "category": "経営・戦略" },
  { "term": "キャッシュフロー", "meaning": "お金の流れ。帳簿上の利益ではなく、実際に手元にある現金の増減のこと。「黒字倒産」を防ぐために最重要", "category": "経営・戦略" },
  { "term": "BS", "meaning": "Balance Sheet（貸借対照表）。会社の資産（現金や土地）と負債（借金）の状態を表す決算書のこと", "category": "経営・戦略" },
  { "term": "PL", "meaning": "Profit and Loss statement（損益計算書）。会社がどれだけ儲かったか、損したかを表す決算書のこと", "category": "経営・戦略" },
  { "term": "MoM / YoY", "meaning": "Month over Month（前月比） / Year over Year（前年比）。売上やユーザー数の成長率を報告する際によく使われる略語", "category": "経営・戦略" },
  { "term": "シナジー", "meaning": "相乗効果。複数の企業や事業が協力することで、単独でやるよりも大きな成果を生み出すこと（1+1が3になるイメージ）", "category": "経営・戦略" },
  { "term": "CAC", "meaning": "Customer Acquisition Cost（顧客獲得単価）。顧客を1人獲得するためにかかった費用のこと（LTVとセットで分析する）", "category": "経営・戦略" },
  { "term": "ガバナンス", "meaning": "企業統治。不正を防ぎ、企業価値を高めるために企業自身を管理・監督する仕組み", "category": "経営・戦略" },
  { "term": "アライアンス", "meaning": "企業同士の提携、協力関係のこと。お互いの強みを活かして事業拡大を目指す戦略", "category": "経営・戦略" },
  { "term": "ARR", "meaning": "Annual Recurring Revenue（年次経常収益）。MRRを12倍して年間の収益規模を表したもの", "category": "経営・戦略" },
  { "term": "MRR", "meaning": "Monthly Recurring Revenue（月次経常収益）。サブスク事業などで、毎月決まって入ってくる売上のこと", "category": "経営・戦略" },
  { "term": "ROI", "meaning": "投資対効果。投資したコストに対して、どれだけの利益が返ってきたかを示す指標（％で表すことが多い）", "category": "経営・戦略" },
  { "term": "カーブアウト", "meaning": "事業の一部を切り出し、外部からの出資などを受け入れて、より独立性の高い企業として再編すること", "category": "経営・戦略" },
  { "term": "スピンオフ", "meaning": "会社の一部門を切り離して、元の会社との関係を保ったまま別会社として独立させること", "category": "経営・戦略" },
  { "term": "FS", "meaning": "実現可能性調査（Feasibility Study）。新規事業などが技術的・採算的に実行可能か事前に調査すること", "category": "経営・戦略" },
  { "term": "KPI", "meaning": "重要業績評価指標。KGI（最終ゴール）を達成するための中間目標。進捗が順調かどうかを測るもの", "category": "経営・戦略" },
  { "term": "PoC", "meaning": "概念実証。新しいアイデアや技術が実現可能か、本格導入前に小規模に試すこと", "category": "経営・戦略" },
  { "term": "KGI", "meaning": "重要目標達成指標。KPIの親にあたる指標で、企業やプロジェクトの最終的なゴール（売上高、利益など）のこと", "category": "経営・戦略" }
]

# Global State
questions = []
current_index = 0
records = []
selected_option = None
is_answered = False

def get_el(id):
    return document.getElementById(id)

def show_screen(screen_id):
    get_el("start-screen").classList.add("hidden")
    get_el("quiz-screen").classList.add("hidden")
    get_el("result-screen").classList.add("hidden")
    
    el = get_el(screen_id)
    el.classList.remove("hidden")
    # Reset opacity animation helper
    el.style.opacity = "0"
    window.setTimeout(create_proxy(lambda: el.style.setProperty("opacity", "1")), 50)

def start_game(event):
    global questions, current_index, records
    try:
        count = int(get_el("question-count-slider").value)
    except:
        count = 10
        
    # Logic to generate quiz
    pool = VOCABULARY_LIST.copy()
    random.shuffle(pool)
    selected_items = pool[:count]
    
    questions = []
    for item in selected_items:
        others = [t["term"] for t in VOCABULARY_LIST if t["term"] != item["term"]]
        distractors = random.sample(others, 3)
        options = distractors + [item["term"]]
        random.shuffle(options)
        
        questions.append({
            "term": item["term"],
            "meaning": item["meaning"],
            "category": item["category"],
            "options": options
        })
        
    current_index = 0
    records = []
    
    show_screen("quiz-screen")
    render_question()

def render_question():
    global is_answered, selected_option
    is_answered = False
    selected_option = None
    
    q = questions[current_index]
    total = len(questions)
    
    # Update UI
    get_el("progress-bar").style.width = f"{(current_index / total) * 100}%"
    get_el("question-number").innerText = f"Question {current_index + 1} / {total}"
    get_el("question-category").innerText = q["category"]
    get_el("question-text").innerText = q["meaning"]
    
    # Hide next button
    get_el("next-button").classList.add("hidden")
    
    # Clear and render options
    container = get_el("options-container")
    container.innerHTML = ""
    
    for opt in q["options"]:
        btn = document.createElement("button")
        btn.className = "w-full p-4 rounded-xl text-left border-2 border-gray-100 hover:border-indigo-200 hover:bg-indigo-50 transition-all duration-200 flex justify-between items-center"
        btn.innerText = opt
        btn.setAttribute("data-option", opt)
        
        # Attach click event
        btn.addEventListener("click", create_proxy(on_option_click))
        container.appendChild(btn)

def on_option_click(event):
    global is_answered, selected_option, records
    if is_answered:
        return
        
    target = event.currentTarget
    selected = target.getAttribute("data-option")
    selected_option = selected
    is_answered = True
    
    q = questions[current_index]
    is_correct = (selected == q["term"])
    
    records.append({
        "question": q,
        "selected": selected,
        "is_correct": is_correct
    })
    
    # Update Styles
    container = get_el("options-container")
    for btn in container.children:
        opt = btn.getAttribute("data-option")
        btn.disabled = True
        
        # Reset base classes
        btn.className = "w-full p-4 rounded-xl text-left border-2 transition-all duration-200 flex justify-between items-center"
        
        if opt == q["term"]:
            # Correct answer
            btn.classList.add("border-green-500", "bg-green-50", "text-green-700", "font-semibold")
            # Add check icon
            icon = document.createElement("div")
            icon.innerHTML = '<svg class="w-5 h-5 text-green-600" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/></svg>'
            btn.appendChild(icon)
        elif opt == selected and not is_correct:
            # Incorrect selection
            btn.classList.add("border-red-500", "bg-red-50", "text-red-700")
            # Add X icon
            icon = document.createElement("div")
            icon.innerHTML = '<svg class="w-5 h-5 text-red-600" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="m15 9-6 6"/><path d="m9 9 6 6"/></svg>'
            btn.appendChild(icon)
        else:
            # Others
            btn.classList.add("border-gray-100", "text-gray-400", "opacity-50")

    # Show Next Button
    btn_text = "結果を見る" if current_index == len(questions) - 1 else "次の問題へ"
    get_el("next-button-text").innerText = btn_text
    get_el("next-button").classList.remove("hidden")

def next_question(event):
    global current_index
    if current_index < len(questions) - 1:
        current_index += 1
        render_question()
    else:
        show_results()

def show_results():
    show_screen("result-screen")
    
    correct_count = len([r for r in records if r["is_correct"]])
    total = len(questions)
    percentage = int((correct_count / total) * 100) if total > 0 else 0
    
    get_el("result-percentage").innerText = f"{percentage}%"
    get_el("result-score-text").innerText = f"{total}問中 {correct_count}問正解"
    
    msg = ""
    if percentage == 100: msg = "完璧です！素晴らしい！"
    elif percentage >= 80: msg = "すごい！高得点です！"
    elif percentage >= 60: msg = "その調子！あと少しです。"
    else: msg = "次はもっと頑張ろう！"
    get_el("result-message").innerText = msg
    
    # Render Review List
    container = get_el("review-container")
    container.innerHTML = ""
    
    for i, r in enumerate(records):
        q = r["question"]
        is_correct = r["is_correct"]
        
        div = document.createElement("div")
        border_class = "border-green-500" if is_correct else "border-red-500"
        
        # Build inner HTML
        html_content = f"""
            <div class="bg-white p-5 rounded-xl shadow-sm border-l-4 {border_class}">
              <div class="flex items-start gap-3">
                <div class="mt-1 flex-shrink-0">
                  {'<svg class="w-6 h-6 text-green-500" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/></svg>' if is_correct else '<svg class="w-6 h-6 text-red-500" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="m15 9-6 6"/><path d="m9 9 6 6"/></svg>'}
                </div>
                <div class="flex-grow">
                  <div class="flex justify-between items-start mb-2">
                    <span class="text-xs font-semibold text-gray-400 uppercase tracking-wider">
                      Q.{i + 1} {q['category']}
                    </span>
                  </div>
                  <p class="text-gray-800 font-medium mb-3">
                    {q['meaning']}
                  </p>
                  
                  <div class="flex flex-col sm:flex-row gap-2 sm:gap-8 text-sm">
                    <div class="flex flex-col">
                      <span class="text-gray-400 text-xs">正解</span>
                      <span class="font-bold text-green-700">{q['term']}</span>
                    </div>
                    {"" if is_correct else f'''
                    <div class="flex flex-col">
                      <span class="text-gray-400 text-xs">あなたの回答</span>
                      <span class="font-bold text-red-600 line-through decoration-red-400 decoration-2">
                        {r['selected']}
                      </span>
                    </div>
                    '''}
                  </div>
                </div>
              </div>
            </div>
        """
        div.innerHTML = html_content.strip()
        container.appendChild(div.firstElementChild)

def restart_game(event):
    get_el("question-count-slider").value = 10
    get_el("count-display").innerText = "10"
    show_screen("start-screen")

# Initialization
get_el("max-count-label").innerText = f"{len(VOCABULARY_LIST)}問 (全問)"
get_el("question-count-slider").max = len(VOCABULARY_LIST)
get_el("loading").style.display = "none"

