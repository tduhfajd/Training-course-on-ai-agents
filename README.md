<div align="center">

# Как решать любые задачи с AI-агентами

**Agent-guided starter kit** — практический курс, который AI-агент проводит вместе с вами на вашей реальной задаче.

За 90 минут: от сырой идеи → к первому полезному результату.

[![GitHub stars](https://img.shields.io/github/stars/tduhfajd/Training-course-on-ai-agents?style=for-the-badge&logo=github)](https://github.com/tduhfajd/Training-course-on-ai-agents/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/tduhfajd/Training-course-on-ai-agents?style=for-the-badge&logo=github)](https://github.com/tduhfajd/Training-course-on-ai-agents/network/members)
[![Last commit](https://img.shields.io/github/last-commit/tduhfajd/Training-course-on-ai-agents?style=for-the-badge&logo=git)](https://github.com/tduhfajd/Training-course-on-ai-agents/commits/main)

[![Markdown](https://img.shields.io/badge/Format-Markdown-000000?style=flat-square&logo=markdown)](#)
[![Language](https://img.shields.io/badge/Язык-Русский-0052CC?style=flat-square)](#)
[![Duration](https://img.shields.io/badge/Первый_проход-90_минут-FF6B35?style=flat-square)](#быстрый-старт-для-ученика)
[![Agent](https://img.shields.io/badge/Формат-Agent--guided-7C3AED?style=flat-square)](#для-агента)
[![License](https://img.shields.io/badge/License-Educational-22C55E?style=flat-square)](#)

[Быстрый старт](#быстрый-старт-для-ученика) · [Теория](course/theory/README.md) · [Практика](course/practice/README.md) · [Контакты](#автор)

</div>

---

## О курсе

Главный фокус — **универсальность подхода**. Один и тот же принцип работает для:

| Сфера | Примеры |
| --- | --- |
| Работа | приложение, отчёт, презентация, анализ данных |
| Учёба | новая тема, конспект, подготовка к встрече |
| Быт и жизнь | поездка, покупка, семейные задачи |
| Творчество | статья, хобби, личный проект |

Курс лучше проходить сразу вместе с агентом. Ученик не просто читает материалы, а просит агента провести его по маршруту [Первый проект за 90 минут](course/first-project-90-min.md). Так сам способ обучения совпадает с тем навыком, который курс развивает.

<details>
<summary><strong>Откуда вырос курс</strong></summary>

<br>

Курс вырос из личного рабочего подхода:

- заводить под задачу отдельную папку или репозиторий;
- фиксировать исходную мысль в `idea.md` или `task.md`;
- вести основную документацию в легких Markdown-файлах;
- складывать рядом все материалы, файлы и источники;
- при необходимости собирать локальную базу знаний;
- обсуждать решение с агентом итеративно;
- использовать навыки, MCP, плагины и инструменты;
- проверять результат и оставлять понятные артефакты.

</details>

## Для кого

- Для членов семьи, которые хотят спокойнее и эффективнее решать бытовые, учебные, творческие и рабочие задачи с ИИ.
- Для коллег, которым нужно быстро перейти от хаотичных запросов к воспроизводимому процессу.
- Для людей без технического бэкграунда, если им показать процесс через понятные жизненные задачи.

## Главная идея

> AI-агенту нужен не идеальный промпт, а хороший рабочий контекст.

Контекст создается не одной длинной командой, а проектной средой: файлами, источниками, описанием цели, ограничениями, решениями, проверками и диалогом.

Вторая важная идея: учиться этому лучше не отдельно от практики, а прямо в процессе решения своей задачи. Агент одновременно помогает выполнить задачу и объясняет, как с ним работать.

Третья важная идея: человек и агент делают разную работу.

| Роль | За что отвечает |
| --- | --- |
| **Человек** | смысл, идеи, предпочтения, эмпатия, творчество, выбор, жизненный контекст |
| **Агент** | структура, скорость, валидация, слабые места, технические шаги, варианты, критика результата |

Отдельно важно: агент хорошо помогает с анализом данных. Если у вас есть таблица, отчет, выгрузка, список заявок или результаты опроса, агент может быстрее найти закономерности, ошибки, выбросы и подготовить понятные выводы.

## Как устроен продукт

Не нужно читать весь репозиторий подряд. Материалы разделены по ролям и моменту использования.

```text
Training-course-on-ai-agents/
├── START_HERE.md          ← вход для агента
├── course/                ← теория, практика, модули, ведущий
├── templates/             ← шаблоны для проектов ученика
├── examples/              ← стартовые промпты и демо
├── exercises/             ← упражнения
└── student-workspace/     ← ваша работа (создаёт агент, в Git не попадает)
```

### Для ученика

1. Сначала прочитать [теоретическую часть](course/theory/README.md).
2. Затем перейти к [практической части](course/practice/README.md).
3. После первого проекта при желании открыть дополнительные [модули](course/modules/).

### Для агента

- [START_HERE.md](START_HERE.md)
- [Первый проект за 90 минут](course/first-project-90-min.md)
- [Стартовый промпт](examples/course-with-agent-prompt.md)

### Для ведущего

- [Материалы для ведущего](course/facilitator/README.md)
- [Гайд ведущего](course/facilitator-guide.md)
- [Чек-лист готовности продукта](course/product-readiness-checklist.md)
- [Дорожная карта](course/roadmap.md)

### Справочные материалы

- [Универсальный подход](course/universal-approach.md)
- [Методика](course/method.md)
- [Технический рабочий процесс](course/technical-workflow.md)
- [Анализ данных с агентом](course/modules/08-data-analysis.md)
- [Шаблоны](templates/)
- [Примеры](examples/)

## Быстрый старт для ученика

```bash
git clone https://github.com/tduhfajd/Training-course-on-ai-agents.git
cd Training-course-on-ai-agents
```

1. Открыть репозиторий в Codex (или другом AI-агенте / IDE с агентом).
2. Написать агенту:

```text
Начни с START_HERE.md и проведи меня по первому проекту за 90 минут
```

3. Агент создает локальную папку `student-workspace/` (исключена из Git).
4. Агент помогает выбрать первую реальную задачу.
5. Внутри `student-workspace/` агент создает папку проекта.
6. Агент копирует туда нужный шаблон: [idea-template.md](templates/idea-template.md) или [task-template.md](templates/task-template.md).
7. Ученик вместе с агентом уточняет задачу, выбирает подход, делает первый результат, проверяет его и фиксирует выводы.

Стартовый запрос также лежит здесь: [course-with-agent-prompt.md](examples/course-with-agent-prompt.md).

## Что считается завершенным первым проходом

После первого прохода в `student-workspace/` есть проект с файлами:

- [x] `idea.md` или `task.md`
- [x] `decisions.md`
- [x] `learning-summary.md`
- [x] первый результат в `results/`
- [x] материалы и база знаний, если они понадобились

Ученик может объяснить базовый цикл:

```text
задача → контекст → вопросы → варианты → выбор → результат → проверка
```

## Проверка продукта

Не объясняйте курс заранее слишком подробно. Лучший тест продукта — дать ученику репозиторий, попросить открыть его в Codex и написать:

```text
Начни с START_HERE.md и проведи меня по первому проекту за 90 минут.
```

Если агент довел ученика до первого результата без ручного спасения процесса, продукт работает.

## Техническая философия

Базовый формат курса — **Markdown**. Такие файлы легко читать, хранить в Git, просматривать в репозитории и редактировать агентом.

Если нужен красивый внешний артефакт, агент может позже собрать из Markdown документ в другом формате: PDF, DOCX, презентацию или страницу. Но источник смысла лучше держать в простых текстовых файлах.

Для работы удобно использовать Codex как агентную среду, а Cursor или VS Code как IDE для просмотра структуры проекта, чтения файлов и ручного редактирования.

---

<div align="center">

## Автор

**Вадим Евграфов**

[![Telegram](https://img.shields.io/badge/Telegram-@vadim__evgrafov-26A5E4?style=for-the-badge&logo=telegram)](https://t.me/vadim_evgrafov)
[![Portfolio](https://img.shields.io/badge/Портфолио-vadimevgrafov.ru-111111?style=for-the-badge&logo=googlechrome&logoColor=white)](https://vadimevgrafov.ru)

| | |
| --- | --- |
| Telegram | [@vadim_evgrafov](https://t.me/vadim_evgrafov) |
| Портфолио | [vadimevgrafov.ru](https://vadimevgrafov.ru) |

<br>

Если курс оказался полезным — поставьте ★ на GitHub.

[![Star this repo](https://img.shields.io/github/stars/tduhfajd/Training-course-on-ai-agents?style=social)](https://github.com/tduhfajd/Training-course-on-ai-agents)

</div>
