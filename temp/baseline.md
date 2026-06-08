# MOUSE System Requirements Baseline Package v2.1

*Monetary Outflow Unified Safeguard Engine — Real-time Behavioral Intervention System*  
*對應技術報告：智慧個人財務決策代理人服務系統｜涵蓋期末 MBSE Task 1–8（§1–9 為凍結 baseline = Task 1–6；§10 = Task 7 追溯＋AI 稽核、§11 = Task 8 變更影響，為對 baseline 之分析與提案，不寫回凍結需求）｜Freeze date: 2026-06-08*

> 本文件由 baseline 工作簿 v2.1 轉出。`[ASSUMED]`/`[INFERRED]`/`[SOURCED]`/`[ADDED]`/`[SUPERSEDED]`/`[RESOLVED]`/`[HUMAN DECISION]` 標記代表資料性質；AI 推斷與待決策彙整於文末。

---

## MOUSE System Requirements Baseline Package v2.1

*Monetary Outflow Unified Safeguard Engine — Real-time Behavioral Intervention System｜對應技術報告：智慧個人財務決策代理人服務系統*

### Baseline Purpose

> 本工作簿為 MOUSE 系統之 System Requirements Baseline Package v2.0，涵蓋期末 MBSE Task 1–5。後續新增需求、調整門檻、修改介面或導入 simulation，皆須經 Change Log 變更控制。

### Baseline Document Index

| No. | Baseline Artifact | Worksheet | Purpose | Owner | Status | Version | Last Updated |
|---|---|---|---|---|---|---|---|
| 1 | Operational Requirements Document / ConOps | 01_ORD_ConOps | mission、stakeholders、OR、success criteria、ConOps、scenarios | Team | Baseline | v2.1 | 2026-06-08 |
| 2 | System Requirements Specification (SRS) | 02_SRS | SRS/PR、rationale、assumption flag、量測門檻、驗證方式 | Requirement Engineer | Baseline | v2.1 | 2026-06-08 |
| 3 | Interface Control Documents (ICD) | 03_ICD | 介面定義 + Linked Requirement（含 v14 外部介面） | Integration Engineer | Baseline | v2.0 | 2026-06-08 |
| 4a | Functional View — Functions | 04a_Functions | 系統功能清單 FUNC-01~08 | System Architect | Baseline | v2.0 | 2026-06-08 |
| 4b | Architecture — Blocks & Allocation | 04b_Allocation | Block 清單 + function→block 配置表 | System Architect | Baseline | v2.0 | 2026-06-08 |
| 5 | Requirements Traceability Matrix (RTM) | 04_RTM | need→OR→SRS→PR→function→block→interface→verification | V&V Engineer | Baseline | v2.0 | 2026-06-08 |
| 6 | Assumptions and Constraints Register | 05_Assumptions_Constraints | 外部前提、限制與 shall not | System Architect | Baseline | v2.0 | 2026-06-08 |
| 7 | Open Items Log | 06_Open_Items | TBD/TBR、owner、target date | Team | Active | v2.0 | 2026-06-08 |
| 8 | Change Log | 07_Change_Log | baseline 版本變更與影響範圍 | Team | Active | v2.1 | 2026-06-08 |
| 9 | AI Decisions & Flags | 08_AI_Decisions_Flags | AI 推斷與待決策（供審查 / AI Usage Log） | Team | Active | v2.1 | 2026-06-08 |
| 10 | Verification View（Task 6） | 09_Verification（§9） | VC-01~06 每條 OR 一案例、method/pass-fail/verifier、RTM handoff、V-OPEN notes | V&V Engineer | Baseline | v2.2 | 2026-06-08 |
| 11 | Traceability + AI Audit（Task 7） | §10 | top-3 數位線索 RTM＋LLM 稽核 12 項發現（含 1 項駁回） | V&V Engineer / Team | Analysis | v2.2 | 2026-06-08 |
| 12 | Change Impact（Task 8 / CHG-006） | §11 | 信用卡回饋來源變更之三層影響＋風險（提案，待核可） | Integration Engineer | Proposed | v2.2 | 2026-06-08 |

### Baseline KPI Summary

| Metric | Value |  | Baseline Rule |
|---|---|---|---|
| Baseline artifacts | 10 |  | Change control |
| SRS / PR entries | 42 |  | Traceability |
| Open TBD / TBR items | 8 |  | Open items |

### Mid-Term → MBSE Weaknesses (Task 1)

| ID | Weakness identified | How MBSE addresses it | Status |
|---|---|---|---|
| W-01 | System Boundary 期中為空白 | 補 context diagram + In/Out/Shall-Not | Resolved v2.0 |
| W-02 | RTM 僅標題；SRS-001/002/003/004/010/011 為孤兒需求 | 補全 RTM 並加 function/block/interface 欄 | Resolved v2.0 |
| W-03 | Verification 僅 method、無正式 case | Task 6 將定義 verification cases | Open (Task 6) |
| W-04 | Out-of-Scope(4) 與 Shall-Not(SRS-017~020) 不一致 | 真人理財/第三方API控制無對應 constraint；折扣碼不在圖 | Open |
| W-05 | PR-ONBD-002 與 PR-BHVR-003 重複；BHVR-005 主觀 | 合併重複需求；補禁用詞庫/UX 驗收 | Open |
| W-06 | 命名 MOUSE/NudgeBudget/技術報告不一致 | v2.0 統一為 MOUSE | Decision pending (F-01) |

### Baseline Freeze / Approval (Task 1)

| Version | v2.1 |
|---|---|
| Freeze Date | 2026-06-08 |
| Approved By | Team（待全組於會議核可） |
| Statement | 本 baseline v2.0 經審查與接受後凍結；任何後續變更須經 Change Log（CHG）登記並評估影響範圍。v1.0 之 CHG-001~003 已核可。 |

---

## 1. Operational Requirements Document (ORD) / ConOps

*MOUSE System baseline v2.0*

### System Mission

> MOUSE 系統的核心命題不是單純記帳，而是透過即時回饋、預警與適度介入，協助使用者改變消費決策行為、降低超支頻率，並逐步建立可持續的財務管理習慣。

### Operational Objectives

| Objective ID | Objective |  | Stakeholder | Type | Primary Need | Interaction |
|---|---|---|---|---|---|---|
| OBJ-01 | 提供即時財務回饋與預警機制 |  | 一般使用者 | Primary | 知道還能花多少、避免超支 | 輸入消費、接收提醒 |
| OBJ-02 | 協助使用者達成預算控制與儲蓄目標 |  | 新鮮人 | Primary | 預算分配引導、冷啟動保護 | 初始設定、接受引導 |
| OBJ-03 | 促進長期健康消費習慣與正向理財誘因 |  | 一般使用者 | Secondary | 系統穩定性、異常處理、參數調整 | 查看消費習慣回饋 |
|  |  |  | LINE Platform | Secondary | 通知可靠性、API 合規 | 推播與訊息通道 |
|  |  |  | 財政部 API | Secondary | 授權與資料正確性 | 電子發票資料 |
|  |  |  | 法規 / 監管機構 | Secondary | 個資、金融法規合規 | 間接約束 |
|  |  |  | 潛在金融服務提供者 | Secondary | 避免越界、自動交易限制 | 間接影響 |

### Operational Requirements (OR)

| OR ID | Theme | Operational Requirement (Why) | Primary Needs | Primary Scenarios | Status | Notes |
|---|---|---|---|---|---|---|
| OR-01 | 避免超支 | 系統 shall 幫助使用者避免於單一發薪週期內發生超支。 | UR-02, UR-03 | Scenario 1, 4 | Baseline | 核心目的 |
| OR-02 | 健康消費習慣 | 系統 shall 引導使用者建立健康消費習慣，使超支頻率逐步下降。 | UR-02, UR-03 | Scenario 1, 2, 4 | Baseline | 強調即時 feedback |
| OR-03 | 理財入門誘因 | 系統 shall 讓使用者看到省錢所帶來的投資與資產成長正向回饋。 | UR-01, UR-04, UR-06 | Scenario 3 | Baseline | 僅提供建議，不自動交易 |
| OR-04 | 新鮮人財務結構 | 系統 shall 在資料不足的初期階段，仍提供基本預算引導與保護。 | UR-05 | Scenario 2 | Baseline | 冷啟動 fallback |

### Operational Scenarios

| Scenario ID | Scenario Name | Trigger | Actor | Main Flow Summary | Alternate / Exception | Related OR |
|---|---|---|---|---|---|---|
| SCN-01 | 月初大額支出型 | 月初支付租金、學費等固定支出 | 一般使用者、MOUSE | 辨識正常固定支出並重新規劃剩餘額度 | 風險分數達 0.85（注意等級）時發送 Warning | OR-01, OR-02 |
| SCN-02 | 新鮮人財務茫然型 | 第一次拿到完整薪水 | 新鮮人、MOUSE | 引導建立預算結構與分類建議 | 72 小時無紀錄時主動確認 | OR-04 |
| SCN-03 | 理財入門誘因型 | 使用者查看省下來的餘額 | 一般使用者、MOUSE | 風險測驗、投資建議、信用卡回饋 | 更新失敗則顯示前一日資料並 retry | OR-03 |
| SCN-04 | 月底危機型 | 第 25 天累積支出達 85% | 一般使用者、MOUSE、ML 模組 | 啟動超支風險預測並發送 Warning | 低於 10% 時升級 Emergency | OR-01 |

### ConOps Summary — How / Who / When

| Dimension | Item | Description |
|---|---|---|
| How | Core pipeline | LINE Bot input → Dedup Engine → Cloud Database → Rule Engine / Prophet ML → Alert Classification → LINE Push |
| Who | Primary actors | 使用者、外部 API、Claude Agent、ML 模組、管理員 |
| When | Immediate | 使用者輸入當下觸發完整 pipeline |
| When | Cold-start milestone | 第 15 個交易日後啟動 ML 預測 |
| When | No record | 72 小時無消費紀錄時，主動確認串接狀況 |

> Operational Success Criteria (MOE / MOP) — Task 2

| ID | Success Criterion | Measure (MOE/MOP) | Target | Source / Flag |
|---|---|---|---|---|
| OSC-01 | 降低超支頻率 | 發薪週期內超支使用者比例 (MOE) | 相對 baseline 下降（目標待定） | [ASSUMED] 需 simulation/問卷驗證 |
| OSC-02 | 預警有效性 | 收到 Warning 後縮減後續支出之使用者比例 (MOE) | 待定 | [ASSUMED] |
| OSC-03 | 風險預警分類效能 | Binary Alarm F1 (MOP) | ≥ 0.85（v14 實測 0.860） | [SOURCED] 技術報告表6 |
| OSC-04 | 控制通知打擾度 | 每使用者每 30 天通知次數 | 等級2≤4 / 等級3≤6 / 等級4≤10 | [SOURCED] 技術報告表4 |
| OSC-05 | 維持記帳持續度 | 使用者連續記帳天數 / 留存 | 待定 | [ASSUMED] |

### Supplementary Operational Requirements (v2.0)

| OR ID | Theme | Operational Requirement (Why) | Primary Needs | Flag |
|---|---|---|---|---|
| OR-05 | 系統營運與維護 | 系統 shall 提供管理員調整風險門檻與通知參數、監控異常並保留 audit trail 之能力。 | 系統管理員 | [ADDED v2.0] 解 admin stakeholder 孤兒 |
| OR-06 | 即時財務決策資訊支援 | 系統 shall 於消費情境中提供即時可用之財務決策資訊（信用卡回饋、金融知識問答、財經新聞摘要）。 | UR-01, UR-04, UR-05, UR-06 | [ADDED v2.0] 涵蓋 v14 新增功能 |

> [HUMAN DECISION] 電子發票自動匯入（SRS-003 / PR-003 / ICD-03）於 v14 技術報告未實作，改為手動 / 真實記帳資料；OR-01 仍成立但匯入來源待團隊決定保留或移除。

---

## 2. System Requirements Specification (SRS)

*SRS = What；PR = How well；所有正式需求使用 shall 語氣。*

| Req ID | Level | OR Source | Requirement Statement | Measure / Threshold | Verification Method | Status | Notes | Rationale | Assumption Flag |
|---|---|---|---|---|---|---|---|---|---|
| MOUSE-SRS-001 | SRS | OR-01 | MOUSE 系統 shall 允許使用者自行設定發薪日作為預算週期起點。 | 合法日期：每月 1–31 日 | 功能測試 | Baseline |  | 支援「避免超支」：即時輸入、匯入、去重、餘額與預警鏈。 |  |
| MOUSE-PR-001 | PR | OR-01 | MOUSE 系統 shall 於設定後 1 秒內完成新週期計算與顯示。 | ≤ 1 秒 | 反應時間測試 | Baseline |  | 支援「避免超支」：即時輸入、匯入、去重、餘額與預警鏈。 |  |
| MOUSE-SRS-002 | SRS | OR-01 | MOUSE 系統 shall 允許使用者透過 LINE Bot 輸入消費紀錄。 | 支援單筆交易輸入 | 功能測試 | Baseline |  | 支援「避免超支」：即時輸入、匯入、去重、餘額與預警鏈。 |  |
| MOUSE-PR-002 | PR | OR-01 | MOUSE 系統 shall 於使用者提交一筆消費紀錄後，於 3 秒內完成接收、解析並回傳結果。 | ≤ 3 秒 | 反應時間測試 | Baseline |  | 支援「避免超支」：即時輸入、匯入、去重、餘額與預警鏈。 |  |
| MOUSE-SRS-003 | SRS | OR-01 | MOUSE 系統 shall 自動匯入使用者授權之電子發票資料。 | 授權後可同步 | 整合測試 | Baseline |  | 支援「避免超支」：即時輸入、匯入、去重、餘額與預警鏈。 | [SUPERSEDED v14] 電子發票匯入未實作 |
| MOUSE-PR-003 | PR | OR-01 | MOUSE 系統 shall 於每次同步作業開始後 5 分鐘內完成最近一期電子發票資料匯入，成功率 shall 達 99% 以上。 | ≤ 5 分鐘；成功率 ≥ 99% | API 整合測試 | Baseline |  | 支援「避免超支」：即時輸入、匯入、去重、餘額與預警鏈。 | [SUPERSEDED v14] 電子發票匯入未實作 |
| MOUSE-SRS-004 | SRS | OR-01 | MOUSE 系統 shall 自動去除重複消費紀錄。 | 比對日期、金額、商家、發票號碼 | 功能測試 | Baseline |  | 支援「避免超支」：即時輸入、匯入、去重、餘額與預警鏈。 |  |
| MOUSE-PR-004 | PR | OR-01 | MOUSE 系統 shall 於新增消費紀錄後 2 秒內完成重複比對，辨識正確率 shall 達 98% 以上。 | ≤ 2 秒；正確率 ≥ 98% | 資料測試 | Baseline |  | 支援「避免超支」：即時輸入、匯入、去重、餘額與預警鏈。 |  |
| MOUSE-SRS-005 | SRS | OR-01 | MOUSE 系統 shall 於消費紀錄成功寫入後即時顯示當期剩餘可用預算。 | 即時顯示 | 功能測試 | Baseline |  | 支援「避免超支」：即時輸入、匯入、去重、餘額與預警鏈。 |  |
| MOUSE-PR-005 | PR | OR-01 | MOUSE 系統 shall 於每筆消費紀錄成功寫入後 1 秒內更新並顯示剩餘預算，誤差不得超過 ±1 元。 | ≤ 1 秒；誤差 ≤ ±1 元 | 反應時間測試 | Baseline |  | 支援「避免超支」：即時輸入、匯入、去重、餘額與預警鏈。 |  |
| MOUSE-SRS-006 | SRS | OR-01 | MOUSE 系統 shall 於偵測到超支風險時，透過 LINE 主動推播通知使用者。 | 主動 Warning 通知 | 通知測試 | Baseline |  | 支援「避免超支」：即時輸入、匯入、去重、餘額與預警鏈。 Warning 以 Risk Score ≥ 0.85 判定。 |  |
| MOUSE-PR-006 | PR | OR-01 | MOUSE 系統 shall 於使用者風險分數（Risk Score）達 0.85（注意等級）時，於 1 分鐘內發送 Warning 通知，送達率 shall 達 95% 以上。 | Risk Score ≥ 0.85（注意等級）；≤ 1 分鐘；送達率 ≥ 95% | 通知 log、情境模擬 | Baseline |  | 支援「避免超支」：即時輸入、匯入、去重、餘額與預警鏈。 | [RESOLVED v2.1] 改採 Risk Score ≥ 0.85（v14 注意等級）；Risk Score = 0.6×消費壓力 + 0.4×現金流風險（技術報告 3.7.5） |
| MOUSE-SRS-007 | SRS | OR-01 | MOUSE 系統 shall 於使用者即將或已無剩餘預算時發送緊急通知。 | Emergency 通知 | 通知測試 | Baseline |  | 支援「避免超支」：即時輸入、匯入、去重、餘額與預警鏈。 |  |
| MOUSE-PR-007 | PR | OR-01 | MOUSE 系統 shall 於剩餘預算低於 10% 或低於 0 元時，於 30 秒內發送 Emergency 通知，送達率 shall 達 99% 以上。 | < 10% 或 < 0 元；≤ 30 秒；送達率 ≥ 99% | 壓力測試 | Baseline |  | 支援「避免超支」：即時輸入、匯入、去重、餘額與預警鏈。 |  |
| MOUSE-SRS-008 | SRS | OR-01 | MOUSE 系統 shall 於累積足夠消費資料後啟動 ML 模型預測使用者超支風險。 | 至少 15 個交易日 | 模型流程測試 | Baseline |  | 支援「避免超支」：即時輸入、匯入、去重、餘額與預警鏈。 | [ASSUMED] 15 交易日門檻待驗證 |
| MOUSE-PR-008 | PR | OR-01 | MOUSE 系統 shall 於累積至少 15 個交易日資料後啟動模型，Recall shall 達 85% 以上，Precision shall 達 75% 以上。 | 交易日 ≥ 15；Recall ≥ 85%；Precision ≥ 75% | 模型驗證 | TBR | simulation 後確認 | 支援「避免超支」：即時輸入、匯入、去重、餘額與預警鏈。 | [ASSUMED] 15 交易日 / Recall/Precision 待 simulation 確認 |
| MOUSE-SRS-009 | SRS | OR-02 | MOUSE 系統 shall 於使用者輸入或匯入消費後即時顯示當期剩餘可用預算。 | 即時餘額回饋 | 功能測試 | Baseline |  | 支援「健康消費習慣」：即時回饋並抑制通知疲勞。 |  |
| MOUSE-PR-009 | PR | OR-02 | MOUSE 系統 shall 於單筆新增或修改紀錄後，於 1 秒內更新並顯示最新餘額，目標值為 0.5 秒。 | 閾值 ≤ 1 秒；目標 ≤ 0.5 秒 | 延遲測試 | Baseline |  | 支援「健康消費習慣」：即時回饋並抑制通知疲勞。 |  |
| MOUSE-SRS-010 | SRS | OR-02 | MOUSE 系統 shall 限制一般預警推播頻率，避免過度打擾使用者。 | 限制一般 Warning 次數 | 功能測試 | Baseline |  | 支援「健康消費習慣」：即時回饋並抑制通知疲勞。 |  |
| MOUSE-PR-010 | PR | OR-02 | MOUSE 系統 shall 將非嚴重超支之一般預警限制為每一太陽曆日最多 1 次。 | 每人每日 ≤ 1 次 | 通知 log 驗證 | Baseline |  | 支援「健康消費習慣」：即時回饋並抑制通知疲勞。 |  |
| MOUSE-SRS-011 | SRS | OR-02 | MOUSE 系統 shall 在使用者長時間無消費紀錄時主動詢問確認狀況。 | 無紀錄提醒 | 情境測試 | Baseline |  | 支援「健康消費習慣」：即時回饋並抑制通知疲勞。 |  |
| MOUSE-PR-011 | PR | OR-02 | MOUSE 系統 shall 於連續 72 小時無新增紀錄或同步動作時，在次日日間主動發送一次確認通知。 | 72 小時；09:00–21:00 | 情境測試 | Baseline |  | 支援「健康消費習慣」：即時回饋並抑制通知疲勞。 |  |
| MOUSE-SRS-012 | SRS | OR-03 | MOUSE 系統 shall 提供投資風險評估測驗，以了解使用者風險承受度。 | 首次設定後邀請 | 功能測試 | Baseline |  | 支援「理財入門誘因」：風險測驗、投資建議與回饋資訊。 |  |
| MOUSE-PR-012 | PR | OR-03 | MOUSE 系統 shall 提供不超過 10 題之風險測驗，提交後 2 秒內回傳分類結果。 | 題數 ≤ 10；回傳 ≤ 2 秒 | 使用者測試 | Baseline |  | 支援「理財入門誘因」：風險測驗、投資建議與回饋資訊。 |  |
| MOUSE-SRS-013 | SRS | OR-03 | MOUSE 系統 shall 根據使用者風險屬性與結餘金額提供投資建議通知。 | 個人化建議 | 流程測試 | Baseline |  | 支援「理財入門誘因」：風險測驗、投資建議與回饋資訊。 |  |
| MOUSE-PR-013 | PR | OR-03 | MOUSE 系統 shall 於每個發薪週期結束後 24 小時內產生個人化投資建議。 | ≤ 24 小時 | 流程測試 | Baseline |  | 支援「理財入門誘因」：風險測驗、投資建議與回饋資訊。 |  |
| MOUSE-SRS-014 | SRS | OR-03 | MOUSE 系統 shall 提供信用卡回饋優惠資訊供使用者參考。 | 回饋資訊查詢 | 功能測試 | Baseline |  | 支援「理財入門誘因」：風險測驗、投資建議與回饋資訊。 |  |
| MOUSE-PR-014 | PR | OR-03 | MOUSE 系統 shall 每 24 小時至少更新一次信用卡回饋資訊，抓取成功率 shall 達 95% 以上。 | 24 小時；成功率 ≥ 95% | 爬蟲 log 驗證 | Baseline |  | 支援「理財入門誘因」：風險測驗、投資建議與回饋資訊。 | [NEEDS SOURCE] 信用卡回饋取得方式之法律可行性待確認 |
| MOUSE-SRS-015 | SRS | OR-04 | MOUSE 系統 shall 在消費紀錄不足時仍提供基本預算上限提醒。 | 冷啟動 fallback | 規則測試 | Baseline |  | 支援「新鮮人冷啟動」：資料不足時仍提供基本保護。 |  |
| MOUSE-PR-015 | PR | OR-04 | MOUSE 系統 shall 於冷啟動期間達預算 80% 時，在 1 分鐘內發送預算提醒，送達率 shall 達 95% 以上。 | 交易日 < 15；80%；≤ 1 分鐘；送達率 ≥ 95% | 規則測試 | Baseline |  | 支援「新鮮人冷啟動」：資料不足時仍提供基本保護。 |  |
| MOUSE-SRS-016 | SRS | OR-04 | MOUSE 系統 shall 在使用者長時間無消費紀錄時主動詢問確認狀況。 | 無紀錄提醒 | 情境測試 | Baseline |  | 支援「新鮮人冷啟動」：資料不足時仍提供基本保護。 |  |
| MOUSE-PR-016 | PR | OR-04 | MOUSE 系統 shall 於連續 72 小時無新增紀錄或同步動作時，在次日日間主動發送一次確認通知。 | 72 小時；09:00–21:00 | 情境測試 | Baseline |  | 支援「新鮮人冷啟動」：資料不足時仍提供基本保護。 |  |
| MOUSE-SRS-017 | SRS | Shall Not | MOUSE 系統 shall not 自動執行任何投資操作。 | 禁止自動交易 | 設計審查 | Baseline | 法規風險 | 源自法規/政策之 constraint，非由 OR 衍生（見 05 register）。 |  |
| MOUSE-SRS-018 | SRS | Shall Not | MOUSE 系統 shall not 處理外幣交易。 | 超出 ODD | 設計審查 | Baseline |  | 源自法規/政策之 constraint，非由 OR 衍生（見 05 register）。 |  |
| MOUSE-SRS-019 | SRS | Shall Not | MOUSE 系統 shall not 將使用者資料提供給第三方。 | 個資限制 | 法規審查 | Baseline |  | 源自法規/政策之 constraint，非由 OR 衍生（見 05 register）。 |  |
| MOUSE-SRS-020 | SRS | Shall Not | MOUSE 系統 shall not 共享使用者折扣碼。 | 法律風險 | 設計審查 | Baseline |  | 源自法規/政策之 constraint，非由 OR 衍生（見 05 register）。 |  |
| MOUSE-SRS-021 | SRS | OR-06 | MOUSE 系統 shall 依使用者輸入解析品牌並查詢信用卡回饋資料庫後以自然語言回覆。 | 命中時回傳結構化回饋 | 功能測試 | Baseline | 支援 OR-06：消費情境即時決策。 | [ADDED v2.0 from v14] |  |
| MOUSE-SRS-022 | SRS | OR-06 | MOUSE 系統 shall 以 RAG 架構檢索 top-3 段落作答，超出範疇時回覆「文件中未提及」。 | 檢索 top-3；越界拒答 | 功能測試 / 抽樣審查 | Baseline | 支援 OR-06：降低 LLM 幻覺。 | [ADDED v2.0] top-3 為 v14 實測設定 |  |
| MOUSE-SRS-023 | SRS | OR-06 | MOUSE 系統 shall 彙整 24 小時內可信來源財經新聞生成摘要，來源不足時以即時搜尋 fallback 並保留引用。 | 24hr 內文章；保留來源 | 功能測試 | Baseline | 支援 OR-06：降低資訊蒐集成本。 | [ADDED v2.0 from v14] |  |
| MOUSE-SRS-024 | SRS | OR-05 | MOUSE 系統 shall 提供管理員調整風險門檻與通知參數之介面。 | 參數可調（範圍 [TBD]） | 功能測試 | Draft | 支援 OR-05：營運維護。 | [ADDED v2.0] 門檻範圍 [TBD] |  |
| MOUSE-SRS-025 | SRS | OR-05 | MOUSE 系統 shall 保留異常事件與管理操作之 audit trail。 | 可追溯記錄 | 檢視 (inspection) | Draft | 支援 OR-05：稽核與異常處理。 | [ADDED v2.0] |  |
| MOUSE-SRS-026 | SRS | OR-06 | MOUSE 系統 shall 維持任務型短期對話記憶（保存 2 小時、最多 10 筆、每筆 ≤500 字，任務完成後清除）。 | 2hr / ≤10 筆 / ≤500 字 | 功能測試 | Baseline | 支援 FUNC-08 多輪對話。 | [ADDED v2.0] 數值為 v14 實測 |  |

---

## 3. Interface Control Documents (ICD)

*ICD baseline v2.0 — 已補 Linked Requirement；ICD-12~14 為 v14 外部介面 [ADDED]。*

| Interface ID | From | To | Data / Message | Trigger | Failure Handling | Status | Owner | Linked Requirement | Key (Top-5) |
|---|---|---|---|---|---|---|---|---|---|
| ICD-01 | 使用者 | LINE Bot | 消費金額、分類、時間、備註 | 使用者提交交易 | 格式錯誤時要求重新輸入 | Baseline | Integration Engineer | SRS-002 | 是 |
| ICD-02 | LINE Bot | Backend | 結構化交易紀錄、User ID | 收到使用者輸入 | API timeout 時 retry 並回傳失敗訊息 | Baseline | Integration Engineer | SRS-002 |  |
| ICD-03 | 財政部 API | Backend | 授權之電子發票資料 | 定期同步或手動同步 | 同步失敗時 retry，並提示手動輸入 | Superseded (v14) | Integration Engineer | SRS-003 [SUPERSEDED v14] |  |
| ICD-04 | 信用卡回饋資料來源 | Backend | 回饋方案、更新時間、適用條件 | 每日更新 | 抓取失敗時顯示前一日資料並 retry | Draft | Integration Engineer | SRS-014, SRS-021 |  |
| ICD-05 | Backend | Dedup Engine | 新增 / 匯入交易紀錄 | 收到交易資料 | 錯誤時寫入 log 並標記待人工處理 | Baseline | Backend Owner | SRS-004 |  |
| ICD-06 | Dedup Engine | Cloud Database | 去重後交易紀錄 | 完成比對 | 寫入失敗則 retry 並保留原始資料 | Baseline | Backend Owner | SRS-004 | 是 |
| ICD-07 | Cloud Database | Layer 1 Rule Engine | 預算、累積支出、剩餘額度 | 每次交易更新 | 資料不完整時使用保守 fallback | Baseline | Rule Engine Owner | SRS-005, SRS-006 | 是 |
| ICD-08 | Cloud Database | Prophet ML Module | 至少 15 個交易日之歷史消費資料 | 冷啟動達標後 | 資料不足時不啟動 ML | TBR | ML Owner | SRS-008 | 是 |
| ICD-09 | Alert Classification Engine | LINE Push API | Warning / Emergency 通知 payload | 達預警門檻 | 推播失敗時 retry，並寫入 log | Baseline | Notification Owner | SRS-006, SRS-007 | 是 |
| ICD-10 | Admin Backend | 系統模組 | 參數調整、異常監控資訊 | 管理員操作 | 保留 audit trail | Draft | Admin Owner | OR-05, SRS-024, SRS-025 |  |
| ICD-11 | Claude Agent | Backend | 消費模式分析、個人化建議草稿 | 週期結束或使用者查詢 | 輸出需經 guardrail 與規則檢查 | TBR | AI Owner | SRS-013, SRS-022, SRS-017(guardrail) |  |
| ICD-12 | Backend | GPT-4o-mini API | 意圖判斷 / 請求解析 | 收到使用者訊息 | 失敗時 fallback 規則 | Draft | AI Owner | SRS-002 |  |
| ICD-13 | Backend | ChromaDB | RAG 查詢向量 / 檢索段落 | 金融問答 | 檢索失敗回「文件未提及」 | Draft | AI Owner | SRS-022 |  |
| ICD-14 | Backend | Perplexity API | 新聞 fallback 搜尋 | RSS 文章不足時 | 逾時則回報來源不足 | Draft | AI Owner | SRS-023 |  |

---

## 4a. Functional View — System Functions (Task 4)

*系統功能 = 做什麼（非怎麼做）。來源：智慧個人財務決策代理人技術報告 v14 表5 與架構章節。*

| Function ID | Function | Description | Trace to OR | Trace to SRS | Flag / Notes |
|---|---|---|---|---|---|
| FUNC-01 | 自然語言收支記錄 | 以 LINE 對話完成記帳 / 改帳，將輸入嵌入日常對話 | OR-01, OR-02 | SRS-002, SRS-009 |  |
| FUNC-02 | 帳務查詢與視覺化 | 近期紀錄、月報、LIFF 儀表板（資產/類別/趨勢） | OR-02 | SRS-005, SRS-009 | LIFF 為 v14 新增 |
| FUNC-03 | 財務風險預測與主動預警 | 預測未來 7 天支出→風險分級→依等級推播 | OR-01 | SRS-006, SRS-007, SRS-008 | 核心數位線索 |
| FUNC-04 | 信用卡回饋推薦 | 品牌正規化→回饋庫查詢→LLM 自然語言回覆 | OR-06, OR-03 | SRS-014, SRS-021 | [ADDED v2.0] |
| FUNC-05 | 金融知識問答 (RAG) | 向量檢索 top-3 段落→GPT 作答，文件約束 | OR-06 | SRS-022 | [ADDED v2.0 from v14] |
| FUNC-06 | 財經新聞摘要 | RSS+市場資料+Perplexity fallback+GPT 摘要 | OR-06 | SRS-023 | [ADDED v2.0 from v14] |
| FUNC-07 | 儲蓄目標與遊戲化 | 願望清單 + 寵物養成式儲蓄挑戰 | OR-03, OR-04 | SRS-012, SRS-015 | 遊戲化為 v14 新增 |
| FUNC-08 | 對話脈絡維持 | 任務型短期記憶（2hr/≤10筆/≤500字，任務後清除） | OR-06 (enabling) | SRS-026 | [ADDED v2.0] enabling function |

### 註（次要 intent，未列入核心功能）

> 所得稅試算、保險測驗：v14 報告 3.5 提及之 intent，不在功能展示表(表5)，[INFERRED] 列為次要，待團隊決定是否納入。

---

## 4b. Architecture View — Blocks & Function→Block Allocation (Task 4)

*Block = 子系統 / 元件。三層式架構（前台 / 中間層 / 後台）。Allocation 將每個功能配置到一或多個 block。*

### System Blocks (BLK)

| Block ID | Block | Layer | Notes |
|---|---|---|---|
| BLK-01 | LINE Bot 互動介面 | 前台 | Messaging / Push API |
| BLK-02 | LIFF 儀表板前端 | 前台 | 視覺化全覽（資產/月報/趨勢/儲蓄挑戰） |
| BLK-03 | Flask 後端 / 意圖路由 | 中間層 | GPT-4o-mini 意圖判斷與功能分派 |
| BLK-04 | 記帳模組 | 中間層 | expense/income intent 寫入與修改 |
| BLK-05 | 風險預警引擎 | 中間層 | BiGRU 推論 + 風險比率 + 通知冷卻 |
| BLK-06 | 信用卡回饋模組 | 中間層 | 品牌解析 + FTS/LIKE 查詢 + GPT |
| BLK-07 | 金融知識 RAG 模組 | 中間層 | embedding + ChromaDB 檢索 + GPT |
| BLK-08 | 財經新聞模組 | 中間層 | RSS + 市場資料 + Perplexity fallback |
| BLK-09 | 願望清單 / 儲蓄挑戰模組 | 中間層 | 遊戲化儲蓄；寫入收支紀錄 |
| BLK-10 | 短期記憶模組 | 中間層 | DB 暫存、時間過期、任務後清除 |
| BLK-11 | 主資料庫 financial_agent | 後台 | MySQL：使用者/收支/願望/風險 |
| BLK-12 | 信用卡回饋資料庫 | 後台 | MySQL：回饋方案（獨立維護） |
| BLK-13 | 向量資料庫 ChromaDB | 後台 | 金融知識向量索引 |

### Function → Block Allocation

| Function ID | Function | Allocated Blocks |
|---|---|---|
| FUNC-01 | 自然語言收支記錄 | BLK-01, BLK-03, BLK-04, BLK-11 |
| FUNC-02 | 帳務查詢與視覺化 | BLK-01, BLK-02, BLK-03, BLK-11 |
| FUNC-03 | 財務風險預測與主動預警 | BLK-03, BLK-05, BLK-11, BLK-01(推播) |
| FUNC-04 | 信用卡回饋推薦 | BLK-01, BLK-03, BLK-06, BLK-12 |
| FUNC-05 | 金融知識問答 (RAG) | BLK-01, BLK-03, BLK-07, BLK-13 |
| FUNC-06 | 財經新聞摘要 | BLK-01, BLK-03, BLK-08 |
| FUNC-07 | 儲蓄目標與遊戲化 | BLK-01, BLK-02, BLK-09, BLK-11 |
| FUNC-08 | 對話脈絡維持 | BLK-03, BLK-10, BLK-11 |

> [INFERRED] 外部相依（GPT-4o-mini、Perplexity、RSS 來源）列為外部介面（見 03_ICD 之 ICD-12~14），非系統 block。

---

## 4. Requirements Traceability Matrix (RTM / NRTM)

*Need → OR → SRS → PR → Function → Block → Interface → Verification（v2.0 補孤兒需求與完整數位線索）*

| Need ID | User Need | OR ID | SRS ID | PR ID | Scenario | Verification | Status | Function | Block | Interface |
|---|---|---|---|---|---|---|---|---|---|---|
| UR-01 | 我想讓我的錢變多 | OR-03 | MOUSE-SRS-013 | MOUSE-PR-013 | SCN-03 理財入門誘因型 | 流程測試 | Baseline | FUNC-04 | BLK-06 | ICD-04 |
| UR-02 | 我想知道我現在還能花多少 | OR-02 | MOUSE-SRS-009 | MOUSE-PR-009 | SCN-01 月初大額支出型 | 功能測試、延遲測試 | Baseline | FUNC-02 | BLK-04/11 | ICD-01 |
| UR-03 | 我快花太多的時候要有人提醒我 | OR-01 | MOUSE-SRS-006 | MOUSE-PR-006 | SCN-04 月底危機型 | 通知 log、情境模擬 | Baseline | FUNC-03 | BLK-05 | ICD-09 |
| UR-03 | 我快花太多的時候要有人提醒我 | OR-01 | MOUSE-SRS-007 | MOUSE-PR-007 | SCN-04 月底危機型 | 壓力測試 | Baseline | FUNC-03 | BLK-05 | ICD-09 |
| UR-04 | 我想知道省下來的錢怎麼用可以錢滾錢 | OR-03 | MOUSE-SRS-012 | MOUSE-PR-012 | SCN-03 理財入門誘因型 | 使用者測試 | Baseline |  |  |  |
| UR-04 | 我想知道省下來的錢怎麼用可以錢滾錢 | OR-03 | MOUSE-SRS-013 | MOUSE-PR-013 | SCN-03 理財入門誘因型 | 流程測試 | Baseline |  |  |  |
| UR-05 | 我不會理財，想要有人帶我開始 | OR-04 | MOUSE-SRS-015 | MOUSE-PR-015 | SCN-02 新鮮人財務茫然型 | 規則測試 | Baseline |  |  |  |
| UR-05 | 我不會理財，想要有人帶我開始 | OR-04 | MOUSE-SRS-016 | MOUSE-PR-016 | SCN-02 新鮮人財務茫然型 | 情境測試 | Baseline |  |  |  |
| UR-06 | 我想知道哪些消費可以拿回饋 | OR-03 | MOUSE-SRS-014 | MOUSE-PR-014 | SCN-03 理財入門誘因型 | 爬蟲 log 驗證 | Baseline | FUNC-04 | BLK-06 | ICD-04 |
| UR-02 | 我想知道我現在還能花多少 | OR-01 | MOUSE-SRS-005 | MOUSE-PR-005 | SCN-01 月初大額支出型 | 反應時間測試 | Baseline | FUNC-02 | BLK-11 | ICD-07 |
| UR-03 | 我快花太多的時候要有人提醒我 | OR-01 | MOUSE-SRS-008 | MOUSE-PR-008 | SCN-04 月底危機型 | 模型驗證 | TBR | FUNC-03 | BLK-05 | ICD-08 |
| UR-02 | 我想知道我現在還能花多少 | OR-01 | MOUSE-SRS-001 | MOUSE-PR-001 | SCN-01 月初大額支出型 | 功能測試 | Baseline | FUNC-01 | BLK-04 | ICD-01 |
| UR-02 | 我想知道我現在還能花多少 | OR-01 | MOUSE-SRS-002 | MOUSE-PR-002 | SCN-01 月初大額支出型 | 功能測試 | Baseline | FUNC-01 | BLK-04 | ICD-01/02 |
| UR-02 | 我想知道我現在還能花多少 | OR-01 | MOUSE-SRS-003 | MOUSE-PR-003 | SCN-01 月初大額支出型 | 整合測試 | Superseded(v14) | FUNC-01 | BLK-03 | ICD-03 |
| UR-02 | 我想知道我現在還能花多少 | OR-01 | MOUSE-SRS-004 | MOUSE-PR-004 | SCN-01 月初大額支出型 | 資料測試 | Baseline | FUNC-01 | BLK-(dedup) | ICD-05/06 |
| UR-03 | 我快花太多的時候要有人提醒我 | OR-02 | MOUSE-SRS-010 | MOUSE-PR-010 | SCN-04 月底危機型 | 通知 log 驗證 | Baseline | FUNC-03 | BLK-05 | ICD-09 |
| UR-03 | 我快花太多的時候要有人提醒我 | OR-02 | MOUSE-SRS-011 | MOUSE-PR-011 | SCN-02 新鮮人財務茫然型 | 情境測試 | Baseline | FUNC-03 | BLK-05 | ICD-09 |
| UR-03(完整鏈) | 我快花太多的時候要有人提醒我 | OR-01 | MOUSE-SRS-006 | MOUSE-PR-006 | SCN-04 月底危機型 | 通知 log、情境模擬 | Baseline | FUNC-03 | BLK-05 | ICD-09 |

---

## 5. Assumptions and Constraints Register

*Assumed items made explicit*

| ID | Type | Assumption / Constraint | Impact | Mitigation / Handling | Owner | Status | Related Artifact |
|---|---|---|---|---|---|---|---|
| AC-01 | Assumption | 使用者已授權電子發票同步。 | 未授權時，自動匯入無法運作。 | 保留手動輸入 fallback。 | Integration Engineer | Baseline | ICD-03 |
| AC-02 | Assumption | LINE Push API 可正常使用。 | API 中斷時預警可能延遲。 | retry、log、必要時提示使用者。 | Notification Owner | Baseline | ICD-09 |
| AC-03 | Assumption | 使用者具備穩定網路連線。 | 資料提交與通知可能延遲。 | 失敗訊息與重送機制。 | Backend Owner | Draft | ICD-02 |
| AC-04 | Assumption | 信用卡回饋資料來源至少每日可更新一次。 | 資訊可能過期。 | 顯示最後更新時間；失敗時保留前一日資料。 | Integration Engineer | Draft | ICD-04 |
| AC-05 | Assumption | ML 模型啟動前至少可累積 15 個交易日資料。 | 初期無法進行個人化預測。 | 以 Layer 1 規則引擎作為 cold-start fallback。 | ML Owner | TBR | PR-008, PR-015 |
| AC-06 | Constraint | MOUSE 系統 shall not 自動執行任何投資操作。 | 避免金融法規與 liability 風險。 | 僅提供建議，不提供交易入口。 | System Architect | Baseline | SRS-017 |
| AC-07 | Constraint | MOUSE 系統 shall not 處理外幣交易。 | 控制 ODD 與初期複雜度。 | 介面明確標示支援範圍。 | System Architect | Baseline | SRS-018 |
| AC-08 | Constraint | MOUSE 系統 shall not 將使用者資料提供給第三方。 | 個資與信任風險。 | 最小權限、資料保護、稽核紀錄。 | System Architect | Baseline | SRS-019 |
| AC-09 | Constraint | MOUSE 系統 shall not 共享使用者折扣碼。 | 法律與權限風險。 | 僅呈現公開優惠資訊。 | System Architect | Baseline | SRS-020 |
| AC-10 | Constraint | 一般 Warning 每日最多 1 次，但 Emergency 不受此限制。 | 需避免通知疲勞，同時確保高風險事件即時通知。 | 在 Alert Classification Engine 中區分等級。 | Notification Owner | Baseline | PR-010 |

---

## 6. Open Items Log — TBDs / TBRs

*Known gaps managed with owners and dates*

| ID | Type | Open Item | Current Direction | Decision Needed | Owner | Target Date | Status |
|---|---|---|---|---|---|---|---|
| OI-01 | TBD | LLM 優先處理哪一種 MBSE 任務？ | Requirement quality checking、traceability generation、conflict detection | 請老師協助確認 MVP 任務範圍 | Team | 2026-06-12 | Open |
| OI-02 | TBD | 是否納入 simulation？ | 比較不同 intervention policy 對超支率的影響 | 請老師確認 simulation 深度與 KPI | Team | 2026-06-12 | Open |
| OI-03 | TBR | Simulation 資料來源 | 先以 synthetic data 建模，再用問卷或公開資料校準 | 確認是否需要真實資料 | Simulation Owner | 2026-06-19 | Open |
| OI-04 | TBR | ML 模型啟動條件 | 第 15 個交易日後啟動 | 需透過 simulation 或資料分析驗證 | ML Owner | 2026-06-26 | Open |
| OI-05 | TBD | 超支後 intervention 方式 | 提醒、每日支出建議、重新分配預算 | 確認是否納入下一版 scope | System Architect | 2026-06-19 | Open |
| OI-06 | TBR | UI 平台選擇 | LINE Bot 為主；Web / App 作為替代方案 | 保留 trade-off 結果與決策理由 | Integration Engineer | 2026-06-12 | In Review |
| OI-07 | TBD | SysML v2 textual notation 是否納入 LLM dataset | 先以簡化 JSON schema 建立資料集 | 請老師確認資料標準深度 | Team | 2026-06-19 | Open |
| OI-08 | TBR | Claude Agent runtime guardrail | 先由規則引擎限制輸出內容，不允許交易操作 | 需補驗證案例 | AI Owner | 2026-06-26 | Open |

---

## 7. Baseline Change Log

*All baseline changes must be recorded and traced.*

| Change ID | Version | Date | Change Description | Reason | Affected Artifacts | Owner | Approval Status |
|---|---|---|---|---|---|---|---|
| CHG-001 | v1.0 | 2026-06-05 | 建立 MOUSE System Requirements Baseline Package 初始版本。 | 將期中成果轉為可持續維護之 baseline。 | All artifacts | Team | Approved (v1.0 freeze) |
| CHG-002 | v1.0 | 2026-06-05 | 新增 UI 平台選擇、LINE mockup 與 trade-off matrix。 | 回應老師對主要 UI 與平台依賴性的建議。 | ORD / ConOps, ICD, RTM | Integration Engineer | Approved (v1.0 freeze) |
| CHG-003 | v1.0 | 2026-06-05 | 將系統定位由預警工具調整為行為介入系統。 | 回應老師對 mission 與系統命題的建議。 | ORD / ConOps, SRS | System Architect | Approved (v1.0 freeze) |
| CHG-004 | v2.0 | 2026-06-08 | 完成 Task 1–5：凍結 baseline、補弱點清單與 success criteria、新增 OR-05/OR-06、建立 Functions/Blocks/Allocation、ICD 補 Linked Requirement 與 ICD-12~14、RTM 補孤兒需求與 Function/Block/Interface 欄、對照 v14 並統一命名為 MOUSE。 | 依期末規格完成 MBSE Task 1–5，並與技術報告 v14 對齊。 | All artifacts | Team / Requirement Engineer | Pending Review |
| CHG-005 | v2.1 | 2026-06-08 | PR-006 之 Warning 觸發門檻由「累積支出達預算 80%」改為「風險分數 Risk Score ≥ 0.85（注意等級）」；同步更新 SCN-01 敘述。 | 對齊 v14 技術報告實際採用之風險分數模型（選項 B）。 | PR-006, SCN-01, SRS-006(rationale) | Requirement Engineer | Pending Review |
| CHG-006 | v2.2（proposed） | 2026-06-08 | 信用卡回饋資料來源由爬蟲改為官方 API／使用者回報；SRS-014/PR-014/SRS-021 修訂，新增 Shall-Not SRS-027 與條件式 SRS-028，更新 ICD-04（+條件式 ICD-15），修訂 VC-03/VC-06＋新增 VC-07（詳見 §11 Task 8）。 | 法務審查：爬蟲取得回饋資料不具法律可行性（閉合 PR-014 `[NEEDS SOURCE]` / §10 AUD-05 / §9.5 V-OPEN-03）。 | SRS, ICD, Functions/Allocation, RTM, AC register, Verification（VC-03/06/07） | Team / Integration Engineer | Pending Review |

---

## 8. AI Decisions & Flags (for human review)

*本表記錄 AI 在補齊 Task 1–5 時所做的推斷與待決策，供團隊確認/覆寫，並作為 AI Usage Log 之輸入。*

| Flag ID | Type | Item | What AI did | Your decision |
|---|---|---|---|---|
| F-01 | [HUMAN DECISION] | 命名 MOUSE / NudgeBudget / 技術報告標題不一致 | 全檔統一為 MOUSE，移除 NudgeBudget | 確認正式名稱 |
| F-02 | [HUMAN DECISION] | v14 系統範圍比 baseline 廣 | 採 v14 全貌，新增 OR-05/OR-06 涵蓋新功能 | 確認範圍 |
| F-03 | [INFERRED] | OR-05 系統營運與維護 | 由「系統管理員」stakeholder need 推得 | 確認措辭 |
| F-04 | [INFERRED] | OR-06 即時財務決策資訊支援 | 由 UR-01/04/05/06 + v14 功能推得 | 確認措辭 |
| F-05 | [SOURCED] | OSC-03 (F1≥0.85)、OSC-04 (通知上限) | 取自 v14 技術報告 表6 / 表4 | 確認引用 |
| F-06 | [ASSUMED] | OSC-01/02/05 目標值 | 標為待定假設，未給確切數字 | 由團隊訂定或保留假設 |
| F-07 | [SUPERSEDED] | 財政部電子發票 API (SRS-003/PR-003/ICD-03/AC-01) | 標記 superseded，未刪除 | 決定保留或移除 |
| F-08 | [RESOLVED] | 門檻 80% vs v14 風險分級 0.85 | 標於 PR-006 flag，建議當 Task 8 題材 | 已採選項 B：改用 Risk Score ≥ 0.85（v2.1，見 CHG-005） |
| F-09 | [ADDED] | SRS-021~026（v14 新功能） | 新增需求，部分 measure 標 [TBD] | 補門檻 / 確認 |
| F-10 | [INFERRED] | Function→Block allocation | 由 v14 三層架構推得 | 審查配置 |
| F-11 | [DROPPED] | 期中次系統 NOTIF/BHVR/ADVS/ONBD | 未出現在 baseline；blocks 改採 v14 架構 | 決定是否映射 |

---
## 9. Task 6 — Verification View

*本節僅新增 Task 6，不修改前述 baseline v2.1 內容。Verification cases 依目前 OR、SRS / PR、Function、Block 與 ICD 狀態建立；尚未決定或缺少來源者保留 `[TBD]`、`[TBR]`、`[ASSUMED]`、`[NEEDS SOURCE]` 標記。*

### 9.1 Verification Method and Verdict Legend

| Item | Allowed Value | Definition |
|---|---|---|
| Verification Method | `test` | 以測試資料或受控輸入實際執行系統，確認輸出是否符合需求。 |
| Verification Method | `analyze` | 分析 log、時間戳、統計值或模型結果，確認量測門檻是否達成。 |
| Verification Method | `inspect` | 檢視介面、設定、文件、資料欄位或輸出內容是否符合規範。 |
| Verification Method | `demo` | 以操作展示方式證明流程可完成。 |
| Verdict | `Pass` | 所有 pass criterion 均達成。 |
| Verdict | `Fail` | 至少一項 pass criterion 未達成。 |
| Verdict | `Inconclusive` | 因資料不足、門檻待定或前置決策未完成，暫時無法判定。 |
| Verdict | `Error` | 驗證執行過程因系統、工具或資料錯誤而中斷。 |
| Execution Status | `Planned` | 尚未執行。 |
| Execution Status | `Executed` | 已執行並可填寫 verdict。 |

---

### 9.2 Verification Case Index — One Case per OR

| Verification Case ID | Linked OR | Linked SRS / PR | Verification Subject | Method | Test Data / Evidence | Pass / Fail Criterion | Verifier | Execution Status | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| VC-01 | OR-01 避免超支 | MOUSE-SRS-006 / MOUSE-PR-006；MOUSE-SRS-007 / MOUSE-PR-007 | FUNC-03；BLK-05 風險預警引擎；BLK-01 LINE Bot；ICD-09 Alert Classification Engine → LINE Push API | `test` + `demo` + `analyze` | 測試帳號、Risk Score 測試值、預算餘額、通知 payload、觸發與送達時間戳、通知 log、LINE 截圖 | Risk Score ≥ 0.85（注意等級）時，1 分鐘內發送 Warning，送達率 ≥ 95%；剩餘預算 <10% 或 <0 元時，30 秒內發送 Emergency，送達率 ≥ 99%；Emergency 不得受一般 Warning 頻率限制抑制。 | V&V Engineer | Planned | 待執行 |
| VC-02 | OR-02 健康消費習慣 | MOUSE-SRS-009 / MOUSE-PR-009；MOUSE-SRS-010 / MOUSE-PR-010；MOUSE-SRS-011 / MOUSE-PR-011 | FUNC-01、FUNC-02、FUNC-03；BLK-04 記帳模組；BLK-11 主資料庫；BLK-05 風險預警引擎；ICD-01、ICD-02、ICD-09 | `test` + `analyze` | 單筆新增 / 修改交易、DB 更新時間、LINE 回覆時間、每日通知 log、72 小時無紀錄測試帳號 | 單筆新增或修改後，最新餘額於 1 秒內更新並顯示，目標 ≤0.5 秒；一般 Warning 每使用者每日最多 1 次；連續 72 小時無新增紀錄或同步動作時，次日日間發送一次確認通知。 | V&V Engineer | Planned | 待執行 |
| VC-03 | OR-03 理財入門誘因 | MOUSE-SRS-012 / MOUSE-PR-012；MOUSE-SRS-013 / MOUSE-PR-013；MOUSE-SRS-014 / MOUSE-PR-014；MOUSE-SRS-017 | FUNC-04、FUNC-07；BLK-06 信用卡回饋模組；BLK-12 信用卡回饋資料庫；ICD-04、ICD-11 | `test` + `inspect` + `analyze` | 風險測驗測試帳號、測驗題目數、分類結果時間戳、建議產出時間、回饋資料更新 log、建議畫面截圖 | 風險測驗題數 ≤10，提交後 2 秒內回傳分類；每個發薪週期結束後 24 小時內產生個人化建議；回饋資訊每 24 小時至少更新一次且抓取成功率 ≥95%；投資建議不得包含自動交易入口。 | Requirement Engineer、V&V Engineer | Planned | 待執行 |
| VC-04 | OR-04 新鮮人財務結構 | MOUSE-SRS-015 / MOUSE-PR-015；MOUSE-SRS-016 / MOUSE-PR-016 | FUNC-03、FUNC-07；BLK-05 風險預警引擎（含 cold-start fallback）；ICD-07、ICD-09 | `test` + `demo` | 交易日 <15 的新帳號、預算使用率測試資料、通知 log、72 小時無紀錄測試帳號、LINE 截圖 | 交易日 <15 且累積支出達預算 80% 時，即使尚未啟用 ML，系統仍於 1 分鐘內發送預算提醒，送達率 ≥95%；連續 72 小時無新增紀錄或同步動作時，次日日間發送一次確認通知。 | V&V Engineer | Planned | 待執行 |
| VC-05 | OR-05 系統營運與維護 | MOUSE-SRS-024；MOUSE-SRS-025 | ICD-10 Admin Backend → 系統模組；audit trail 儲存機制 | `demo` + `inspect` | 管理員測試帳號、參數修改紀錄、異常事件紀錄、audit trail、畫面截圖 | 管理員可調整風險門檻與通知參數；每次修改均保留 actor、timestamp、changed field、before value、after value；異常事件可追溯。參數允許範圍目前為 `[TBD]`，範圍未決前該部分 verdict 應記為 `Inconclusive`。 | Admin Owner、V&V Engineer | Planned | 待執行 |
| VC-06 | OR-06 即時財務決策資訊支援 | MOUSE-SRS-021；MOUSE-SRS-022；MOUSE-SRS-023；MOUSE-SRS-026 | FUNC-04、FUNC-05、FUNC-06、FUNC-08；BLK-06、BLK-07、BLK-08、BLK-10、BLK-12、BLK-13；ICD-04、ICD-12、ICD-13、ICD-14 | `test` + `inspect` + `analyze` | 品牌查詢測試集、RAG 問答測試集、越界問題、新聞來源與時間戳、fallback 紀錄、短期記憶 session log | 品牌命中時回傳結構化信用卡回饋；RAG 檢索 top-3 段落後作答，越界時回覆「文件中未提及」；新聞摘要使用 24 小時內來源，來源不足時啟用 fallback 並保留引用；短期記憶保存 ≤2 小時、最多 10 筆、每筆 ≤500 字，任務完成後清除。 | AI Owner、Integration Engineer、V&V Engineer | Planned | 待執行 |

---

### 9.3 Detailed Verification Case — VC-01 Overspending Risk Alert and Emergency Notification

#### Basic Information

| Field | Content |
|---|---|
| Verification Case ID | VC-01 |
| Linked OR | OR-01：避免超支 |
| Linked SRS / PR | MOUSE-SRS-006 / MOUSE-PR-006；MOUSE-SRS-007 / MOUSE-PR-007 |
| Verification Subject | FUNC-03 財務風險預測與主動預警；BLK-05 風險預警引擎；BLK-01 LINE Bot；ICD-09 Alert Classification Engine → LINE Push API |
| Objective | 驗證系統是否能依照 Risk Score 與剩餘預算狀態正確區分 Warning / Emergency，並於規定時間內完成 LINE 推播。 |
| Method | `test` + `demo` + `analyze` |
| Verifier | V&V Engineer |
| Execution Status | Planned |
| Verdict | 待執行 |

#### Preconditions

1. 測試帳號已完成 LINE Bot 綁定。
2. 測試帳號已設定單一發薪週期預算。
3. BLK-05 風險預警引擎與 ICD-09 LINE Push API 可正常使用。
4. 系統已啟用交易紀錄、Risk Score、通知觸發時間、送達時間與 error log。
5. 一般 Warning 與 Emergency 可由 Alert Classification Engine 區分。
6. Risk Score 計算依 baseline v2.1：`Risk Score = 0.6 × 消費壓力 + 0.4 × 現金流風險`。

#### Controlled Test Data

| Test Step | Risk Score | Remaining Budget | Expected Notification | Expected Time Limit | Purpose |
|---|---:|---:|---|---|---|
| Step 1 | 0.70 | 30% | 不發送 Warning / Emergency | N/A | 驗證未達門檻時不誤報 |
| Step 2 | 0.85 | 20% | Warning | ≤ 1 分鐘 | 驗證 Risk Score 注意等級門檻 |
| Step 3 | 0.92 | 8% | Emergency | ≤ 30 秒 | 驗證剩餘預算低於 10% 時升級 |
| Step 4 | 0.92 | -5% | Emergency | ≤ 30 秒 | 驗證已超支時緊急通知 |
| Step 5 | 0.90 | 8% | Emergency | ≤ 30 秒 | 同一日已發過 Warning 後再次測試，確認 Emergency 不受 Warning 每日上限抑制 |

#### Verification Procedure

1. 建立測試帳號並完成 LINE Bot 綁定。
2. 對每一組 controlled test data 輸入對應之 Risk Score 與剩餘預算狀態。
3. 紀錄資料寫入時間、分類完成時間、推播觸發時間與使用者端送達時間。
4. 檢查通知類型是否符合預期。
5. 檢查同一日 Warning 頻率限制是否正常運作。
6. 檢查 Emergency 是否可略過一般 Warning 頻率限制。
7. 重複執行 Warning 與 Emergency 測試，以計算送達率。
8. 保留通知 log、交易紀錄、錯誤紀錄與 LINE 截圖。

#### Pass / Fail Criteria

| ID | Criterion | Pass Condition |
|---|---|---|
| VC-01-C01 | Warning 觸發門檻 | Risk Score ≥0.85（注意等級）時觸發 Warning。 |
| VC-01-C02 | Warning 時效 | Warning 於 1 分鐘內送達。 |
| VC-01-C03 | Warning 可靠度 | Warning 送達率 ≥95%。 |
| VC-01-C04 | Emergency 觸發門檻 | 剩餘預算 <10% 或 <0 元時觸發 Emergency。 |
| VC-01-C05 | Emergency 時效 | Emergency 於 30 秒內送達。 |
| VC-01-C06 | Emergency 可靠度 | Emergency 送達率 ≥99%。 |
| VC-01-C07 | 優先權 | Emergency 不得受一般 Warning 每日上限影響。 |
| VC-01-C08 | 誤報控制 | Risk Score <0.85 且剩餘預算 ≥10% 時，不得發送 Warning / Emergency。 |

#### Evidence to Retain

- 測試輸入紀錄
- Risk Score 與剩餘預算狀態
- Alert classification 結果
- LINE Push API payload
- 通知觸發與送達時間戳
- 成功 / 失敗次數與送達率計算
- LINE 通知截圖
- Error log

---

### 9.4 Task 7 RTM Handoff — Verification Case Mapping

*本表供 Task 7 將 Verification Case 接到 digital thread 最末端；未修改前述 RTM。*

| Digital Thread Priority | Need | OR | SRS / PR | Function | Block | Interface | Verification Case |
|---|---|---|---|---|---|---|---|
| Top-1 | UR-03 我快花太多的時候要有人提醒我 | OR-01 | MOUSE-SRS-006 / MOUSE-PR-006 | FUNC-03 | BLK-05 | ICD-09 | VC-01 |
| Top-2 | UR-02 我想知道我現在還能花多少 | OR-02 | MOUSE-SRS-009 / MOUSE-PR-009 | FUNC-02 | BLK-04 / BLK-11 | ICD-01 / ICD-02 | VC-02 |
| Top-3 | UR-06 我想知道哪些消費可以拿回饋 | OR-06 | MOUSE-SRS-021 | FUNC-04 | BLK-06 / BLK-12 | ICD-04 | VC-06 |

---

### 9.5 Verification Review Notes for Task 7 AI Audit

*下列項目由 Task 6 建立 verification cases 時發現。此處僅新增 review notes，不覆寫前述 Open Items Log。*

| Review Note ID | Type | Finding | Why It Matters | Recommended Follow-up |
|---|---|---|---|---|
| V-OPEN-01 | `[TBD]` | SRS-024 的管理員可調參數範圍尚未定義。 | VC-05 無法對允許範圍做 pass / fail 判定。 | 由 System Architect 與 Admin Owner 定義最小值、最大值與權限。 |
| V-OPEN-02 | `[INTERFACE / BLOCK GAP]` | ICD-07 提到 Layer 1 Rule Engine，但 Architecture Blocks 未單獨列出對應 BLK；ICD-10 的 Admin Backend 亦未對應獨立 BLK。 | VC-04、VC-05 與 Task 7 RTM 無法形成完全一致的 block trace。 | Task 7 AI Audit 時確認：新增獨立 block，或註明併入 BLK-05 / BLK-03。 |
| V-OPEN-03 | `[NEEDS SOURCE]` | 信用卡回饋資料來源與合法取得方式仍待確認。 | VC-03、VC-06 的更新成功率與資料正確性可能無法可靠驗證。 | 由 Integration Engineer 確認資料來源與使用條款。 |
| V-OPEN-04 | `[ASSUMED / TBR]` | MOUSE-PR-008 的 15 個交易日、Recall ≥85%、Precision ≥75% 尚待 simulation 或資料分析確認。 | 模型驗證案例不能直接視為 baseline 已通過。 | 額外建立模型驗證子案例，並於 simulation 後更新門檻。 |
| V-OPEN-05 | `[SUPERSEDED]` | MOUSE-SRS-003 / PR-003 / ICD-03 電子發票自動匯入在 v14 未實作。 | 若保留在 scope，需額外建立整合驗證；若移除，需做 change impact。 | 團隊決定保留、延後或移除。 |
| V-OPEN-06 | `[HUMAN DECISION]` | OR-03 與 OR-06 均涵蓋信用卡回饋，但目的不同：理財誘因 vs. 即時決策資訊。 | VC-03 與 VC-06 的驗證範圍可能重疊。 | Task 7 RTM 中保留不同 rationale，避免誤合併。 |

---

### 9.6 Verification Execution Record Template

| Verification Case ID | Execution Date | Tester | Environment / Version | Evidence Link or File | Criterion Result Summary | Verdict | Defect / Issue ID | Notes |
|---|---|---|---|---|---|---|---|---|
| VC-01 |  |  |  |  |  |  |  |  |
| VC-02 |  |  |  |  |  |  |  |  |
| VC-03 |  |  |  |  |  |  |  |  |
| VC-04 |  |  |  |  |  |  |  |  |
| VC-05 |  |  |  |  |  |  |  |  |
| VC-06 |  |  |  |  |  |  |  |  |

---

## 10. Task 7 — Traceability View + AI Audit

*本節對前述凍結 baseline（§1–9）做追溯整合與 AI 稽核，不改寫 baseline 內容。*
*方法依據（INCOSE SE Handbook 4e）：§9.4.2.6 Manage Requirements Traceability（維持 bidirectional traceability）；驗證方法限四標準法 Inspection/Analysis/Demonstration/Test（即 §9.1 之 inspect/analyze/demo/test）。*

### 10.1 Part A — Traceability RTM（完整數位線索）

依規格「demonstrate the chain for your top 2–3 requirements」與 "depth over breadth"。三條 top thread 直接採用 §9.4 之 handoff 對應，各展完整鏈 **need → OR → SRS → PR → function → block → interface → verification case**。

| Thread | Need (UR) | OR | SRS / PR | Function | Block | Interface (ICD) | Verification Case（§9.2） | 狀態 |
|---|---|---|---|---|---|---|---|---|
| **T1 — 超支預警（核心線索）** | UR-03 我快花太多的時候要有人提醒我 | OR-01 避免超支 | SRS-006 / PR-006（RS≥0.85，≤1min，送達≥95%） | FUNC-03 財務風險預測與主動預警 | BLK-05 風險預警引擎（+BLK-01 推播） | **ICD-09** Alert Classification → LINE Push | **VC-01**（test+demo+analyze） | 鏈完整 |
| **T2 — 即時剩餘預算/健康消費** | UR-02 我想知道我現在還能花多少 | OR-02 健康消費習慣 | SRS-009 / PR-009（寫入後 ≤1s 更新餘額，目標 0.5s） | FUNC-02 帳務查詢與視覺化（+FUNC-01） | BLK-04 記帳模組 / BLK-11 主資料庫 | **ICD-01 / ICD-02** 使用者→LINE Bot→Backend | **VC-02**（test+analyze） | 鏈完整 |
| **T3 — 信用卡回饋** | UR-06 我想知道哪些消費可以拿回饋 | OR-06 即時財務決策資訊 | SRS-021（品牌解析→查回饋庫→自然語言回覆） | FUNC-04 信用卡回饋推薦 | BLK-06 信用卡回饋模組（+BLK-12 回饋DB） | **ICD-04** 信用卡回饋資料來源 → Backend | **VC-06**（test+inspect+analyze） | 鏈完整，但資料來源帶 `[NEEDS SOURCE]`（§9.5 V-OPEN-03 / PR-014）→ 由 §11 Task 8 處理 |

**完整鏈（T1，供簡報走查）**：
`UR-03 → OR-01 → MOUSE-SRS-006 / MOUSE-PR-006 → FUNC-03 → BLK-05（+BLK-01）→ ICD-09 → VC-01`
— 從 stakeholder need 一路可追溯至 verification case VC-01（pass 準則見 §9.3）；雙向上 VC-01 亦反向追溯回 SRS-006/007 與 OR-01。

**RTM 覆蓋與已知缺口（不靜默截斷）**：
- 已閉合（完整鏈至 VC）：T1（VC-01）、T2（VC-02）、T3（VC-06）。§9 已為每條 OR 建 VC-01~06，故 RTM verification 欄現可全數指向正式 case（解決 W-03）。
- VC-05（OR-05）因 SRS-024 參數範圍 `[TBD]`（V-OPEN-01）暫 Inconclusive。
- RTM 中 UR-04、UR-05 列之 Function/Block/Interface 欄為空（見 AUD-01）。
- ICD-07 之 Layer 1 Rule Engine、ICD-10 之 Admin Backend 無對應獨立 BLK（見 AUD-12 / V-OPEN-02）。

### 10.2 Part B — AI Audit of the RTM

**稽核者**：LLM（Claude）。**對象**：§1–9。**維度**：missing links、weak language、hidden assumptions、contradictory requirements、interface gaps。
**治理原則（規格 §2）**：AI 為 reviewer，不得發明事實或門檻；採納／拒絕由人類裁決並記錄理由。與 §9.5 V-OPEN 之分工：本節不重複，交叉引用既有 V-OPEN、補 RTM 層級新發現、並保留一項 AI 誤判被駁回之紀錄。

**稽核 prompt（摘要，供 AI Usage Log）**：
> 「以 INCOSE 之 traceability 與 requirement quality 準則，稽核此 RTM 與其 SRS/ICD/VC：找出 (1) 缺漏 trace、(2) 不可驗證／主觀語言、(3) 隱藏假設、(4) 矛盾需求、(5) 介面缺口。標明哪些屬規格禁止之『AI 自行發明門檻』而需人工裁決。」

| Finding | 維度 | AI 發現（位置） | AI 建議 | 人類裁決 | 對應 V-OPEN |
|---|---|---|---|---|---|
| **AUD-01** | Missing link | RTM 中 UR-04（SRS-012/013）、UR-05（SRS-015/016）列 Function/Block/Interface 欄為空 | SRS-012/013→FUNC-07/BLK-09；SRS-015/016→FUNC-03+07／BLK-05／ICD-09（與 VC-04 一致） | **Accepted（補鏈）** | 新發現 |
| **AUD-02** | Interface gap | FUNC-08（SRS-026 / BLK-10 短期記憶）於 ICD 無對應介面 | 新增 ICD：BLK-03 ↔ BLK-10（記憶讀寫、過期清除） | **Accepted（Open）** | 新發現 |
| **AUD-03** | Weak language | SRS-005/SRS-009「即時」單獨不可驗證 | 以 PR-005/PR-009（≤1s、±1元）承載門檻；VC-02 已據此判定 | **Modified（不改 baseline）** | 新發現 |
| **AUD-04** | Hidden assumption | SRS-008/PR-008「15 交易日」「Recall≥85%/Precision≥75%」為 `[ASSUMED]`/TBR | 以 simulation／資料驗證，VC 維持 Inconclusive | **Accepted** | **= V-OPEN-04** |
| **AUD-05** | Hidden assumption | PR-014 隱含「爬蟲取得回饋資料為合法」（`[NEEDS SOURCE]`） | 取得法律意見；確認前不得當 Baseline 驗證 | **Accepted → 升級為 §11 Task 8（CHG-006）** | **= V-OPEN-03**（最高價值） |
| **AUD-06** | Hidden assumption | OSC-01/02/05 目標「待定」`[ASSUMED]`——success criteria 未量化 | 由團隊以問卷／simulation 訂 MOE 目標 | **Accepted（Open）** | 新發現 |
| **AUD-07** | Redundancy | SRS-011 與 SRS-016（PR-011≡PR-016）重複，掛於不同 OR | 合併為單一需求，由 OR-02 與 OR-04 共同追溯 | **Accepted（Open，= W-05）** | 新發現 |
| **AUD-08** | Scope 一致性 | Out-of-Scope(4) 與 Shall-Not(SRS-017~020) 不一致（W-04） | 補對應 Shall-Not／更新邊界圖 | **Accepted（部分由 CHG-006 之 SRS-027 閉合）** | 新發現 |
| **AUD-09** | Weak language | SRS-024「參數可調（範圍 [TBD]）」不可驗證；VC-05 因此 Inconclusive | 補門檻範圍後方可定 verdict | **Accepted（保留 [TBD]）** | **= V-OPEN-01** |
| **AUD-10** | Stale status | SRS-003/PR-003 標 `[SUPERSEDED v14]` 但 Status 仍「Baseline」 | 改 Superseded 或退役，並決定 import 來源 | **Accepted（Open，[HUMAN DECISION]）** | **= V-OPEN-05** |
| **AUD-11** | （疑似）Contradiction | PR-010「一般 Warning 每日 ≤1」 vs PR-006「RS≥0.85 即時發 Warning」 | （AI 初判矛盾，建議調和） | **Rejected** — 非矛盾：AC-10 已定 Emergency 不受上限、PR-010 僅限「非嚴重一般預警」，VC-01-C07 已驗此優先權。**AI 誤判，人工駁回** | 治理示例 |
| **AUD-12** | Block gap | ICD-07 Rule Engine、ICD-10 Admin Backend 無對應獨立 BLK | 新增 BLK 或註明併入 BLK-05/BLK-03 | **Accepted（Open）** | **= V-OPEN-02** |

**稽核小結**：12 項——Accepted 9、Modified 1、Rejected 1（AUD-11，AI 自身誤判，保留以示人類治理）。新發現（§9.5 未涵蓋）：AUD-01/02/06/07/08；與 §9.5 交叉確認：AUD-04/05/09/10/12。最高價值 AUD-05（=V-OPEN-03）升級為 Task 8。

**AI Usage Log 片段（本次稽核）**：

| Prompt 目的 | AI 輸出 | 採納 | 拒絕／修正 | 發現之 AI 風險 |
|---|---|---|---|---|
| 稽核 RTM 五維度 | 12 項發現 | AUD-01~10、12 | AUD-11（誤判矛盾）駁回 | AI 易把受 AC-10 條件約束之需求誤讀為矛盾——需人類掌握 constraint register 全貌 |
| 建議補門檻（SRS-024/OSC） | 提議具體數值 | 否 | 全數拒絕填值，標 [TBD]/[ASSUMED] | AI 傾向「發明 performance target」，違反規格 §2，必須人工把關 |

---

## 11. Task 8 — Scope One Change Impact

*以正式變更 CHG-006 登記於 §7 Change Log（Pending Review）；本節為其三層影響分析，不寫回凍結需求。*

### 11.1 變更請求 CHG-006

| 欄位 | 內容 |
|---|---|
| **Change ID** | CHG-006 |
| **Trigger** | §10 AUD-05 ＝ §9.5 V-OPEN-03 / PR-014 `[NEEDS SOURCE]`：法務審查結論——以**爬蟲**取得信用卡回饋資料不具法律可行性 |
| **Change Type（規格三類）** | **New constraint（法規）** |
| **Change Statement** | MOUSE 系統 **shall not** 以未經授權之爬蟲方式取得第三方信用卡回饋資料；資料來源改為 **(a) 官方合作回饋 API** 或 **(b) 使用者自行回報並經驗證** |
| **INCOSE Change Class** | **Class I**（影響 FUNC-04 實現方式、資料來源與法規合規）→ 需 CCB／全組核可 |
| **Affected Documentation** | SRS(§2)、ICD(§3)、Functions/Allocation(§4a/4b)、RTM(§4)、AC register(§5)、Verification(§9：VC-03、VC-06) |
| **Approval Status** | Pending Review |

### 11.2 三層影響追溯（exactly three layers）

**(a) Layer 1 — 需求變更/新增**

| Req ID | 動作 | 變更內容 | Flag |
|---|---|---|---|
| SRS-014 | Retained / rationale 更新 | 行為不變，資料來源由爬蟲改為官方 API／使用者回報 | [REVISED] |
| PR-014 | Revised | 移除「爬蟲抓取成功率 ≥95%」；改為「自授權來源／使用者回報，每 24h 更新，正確率 ≥[TBD]」；清除 `[NEEDS SOURCE]` | [REVISED]→[RESOLVED] |
| SRS-021 | Retained / note 更新 | 邏輯不變，僅資料來源 provenance 更新 | [REVISED-note] |
| **SRS-027（新增）** | Added（Shall-Not） | 「shall not 以未經授權之爬蟲方式取得第三方信用卡回饋資料。」（順帶閉合 W-04 之一項） | [ADDED] |
| **SRS-028（新增，條件式）** | Added | (a)「shall 透過授權之官方回饋資料介面取得資料」或 (b)「shall 允許使用者回報並驗證回饋資訊」 | [ADDED] **[HUMAN DECISION REQUIRED]** 路徑 |

§5 連動：AC-04 mitigation 重寫；新增 **AC-11 = Constraint**「回饋資料僅得來自授權來源」對應 SRS-027。

**(b) Layer 2 — block / interface 受影響**

| Block / Interface | 動作 | 影響內容 |
|---|---|---|
| **BLK-06** 信用卡回饋模組 | Modified | 攝取由爬蟲改為官方 API client／使用者回報；品牌解析＋查詢＋GPT 不變 |
| **BLK-12** 信用卡回饋資料庫 | Modified | 填充機制改變；schema 可能加 `source`/`verified`/`valid_until` |
| **ICD-04** | Revised | From 改為「官方回饋 API／使用者回報」；Trigger 改 API 排程或使用者提交；Failure handling 改 API 授權失敗告警／使用者回報欄位驗證 |
| **ICD-15（新增，條件式）** | Added（若選 b） | 使用者 → BLK-06：回饋回報 payload＋驗證結果 |

FUNC-04 之 Allocation block 清單不變（仍 BLK-01/03/06/12），僅 BLK-06 內部實作與 ICD-04 語意更新。

**(c) Layer 3 — verification case 必須更新（對應 §9.2）**

| VC | 動作 | 更新內容 |
|---|---|---|
| **VC-03**（OR-03，含 SRS-014/PR-014） | Revised | 「每 24h 更新且**爬蟲**抓取成功率 ≥95%」改為「自**授權來源／使用者回報**更新，成功率／正確率 ≥[TBD]」；method 之爬蟲 log 檢視改為官方 API 整合測試＋**來源授權文件之 inspect** |
| **VC-06**（OR-06，含 SRS-021） | Revised | 回饋資料來源 evidence 由爬蟲 log 改為授權來源紀錄；其餘不變 |
| **VC-07（新增）** | Added | 對 SRS-027（Shall-Not）：**inspect / design review** 確認系統不含爬蟲元件、回饋資料僅來自授權來源 |

> §9.5 之 **V-OPEN-03** 因本變更而閉合（資料來源確立），可由 Open 改為 Resolved。

### 11.3 變更引入之風險

| 面向 | 風險 | 等級 | 備註 |
|---|---|---|---|
| 時程／成本 | 官方 API 需洽談授權（lead time＋可能授權費）；使用者回報路徑需投入 UX 與驗證 | 中 | Class I，需排程與預算評估 |
| 技術／覆蓋率（MOP） | 回饋覆蓋卡別與更新即時性可能下降 → OR-06 / OR-03 效果部分弱化 | 中 | 建議新增 MOP「回饋覆蓋卡別數／更新延遲」 |
| 資料品質（若選 b） | 使用者回報可能填錯 → 需驗證規則 | 中 | 由 VC-07／驗證規則緩解 |
| 合規（正向） | 消除原 `[NEEDS SOURCE]` 法律風險（閉合 V-OPEN-03）；SRS-027 順帶補 W-04 之一項 | 低（改善） | 本變更主要效益 |
| 未決 | 路徑 (a)/(b)/hybrid 之選擇 `[HUMAN DECISION REQUIRED]` | — | Owner：Integration Engineer／Product；Target：[TBD] |

> 不要求 full re-analysis：嚴格限於 3 層＋風險；ConOps、scenarios 不受實質影響，不重掃。

---

## 數位線索一句話總結（供 Final Presentation 走查）

**UR-03「我快花太多時要有人提醒我」→ OR-01 → SRS-006/PR-006（RS≥0.85, ≤1min, ≥95%）→ FUNC-03 風險預警 → BLK-05 風險引擎 → ICD-09 LINE Push → VC-01（test+demo+analyze，pass 準則見 §9.3）**：一條從 stakeholder need 到 verification case 的完整可追溯鏈。AI 稽核（AUD-05 / V-OPEN-03）在 T3 回饋 thread 上揪出 `[NEEDS SOURCE]` 法律假設，升級為 CHG-006，三層影響（需求／架構介面／VC-03·06·07）＋風險完整追溯——展示「AI 找出 inconsistency、人類做工程決策（含駁回 AI 誤判 AUD-11）、變更被可追溯地治理」。

---
