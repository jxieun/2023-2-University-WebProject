# MusicStory 🎵
<img width="281" height="68" alt="스크린샷 2026-01-18 오전 11 59 32" src="https://github.com/user-attachments/assets/8b1eeffe-a3c9-4bfc-808c-ce7c936ba05b" />


> **웹표준기술 수행과제** - 음악을 좋아하는 누구나 즐길 수 있는 블로그

🚀 **배포 주소**: [https://jxieun.github.io/2023-2-University-WebProject/](https://jxieun.github.io/2023-2-University-WebProject/)

## 📝 프로젝트 소개
**MusicStory**는 HTML/CSS/jQuery의 기초를 다지기 위해 제작한 정적 웹사이트입니다.  
다양한 장르의 음악을 소개하고, 추천하며, 투표할 수 있는 커뮤니티형 블로그를 주제로 하였습니다.

## 🛠 사용 기술 (Tech Stack)
- **HTML5**: 시멘틱 태그(`header`, `nav`, `section`, `article`, `footer` 등)를 활용한 구조 설계
- **CSS3**:
    - `float` 및 `flex` 속성을 이용한 레이아웃 구성
    - `position` (relative, absolute)을 이용한 드롭다운 메뉴 구현
    - 다양한 스타일링 및 마우스 호버 효과
- **jQuery**: 간단한 동적 기능 구현

## ✨ 주요 기능
- **드롭다운 네비게이션**: 마우스를 올리면 하위 메뉴가 나타나는 인터랙션
- **카테고리별 페이지**: 장르별, 주제별, 신곡 등 다양한 카테고리 페이지 연결
- **검색창 UI**: 직관적인 헤더 검색 바 디자인
- **소개 페이지**: `Introduce.html`을 통해 사이트의 목적과 소개를 볼 수 있음

## 📂 프로젝트 구조 (Project Structure)
프로젝트의 유지보수성을 높이기 위해 폴더 구조를 다음과 같이 개편하였습니다.

```
web/
├── index.html          # 메인 페이지
├── css/
│   └── style.css       # 메인 스타일시트
├── assets/
│   └── images/         # 이미지 리소스 중앙 관리
│       ├── genre/      # 장르별 이미지
│       ├── theme/      # 주제별 이미지
│       ├── pages/      # 각 페이지별 리소스
│       └── misc/       # 기타 공용 이미지
└── pages/              # 서브 페이지 (기능별 그룹화)
    ├── genre/          # 장르별 음악 소개
    ├── theme/          # 주제별 음악 추천
    ├── new/            # 신곡 (국내/해외)
    ├── recommend/      # 추천/TOP10/오늘의 음악
    ├── vote/           # 투표 페이지
    └── about/          # 사이트 소개 (Introduce.html)
└── scripts/            # 유지보수 및 자동화 스크립트
    └── refactor_paths.py # 프로젝트 구조 변경 시 경로 자동 수정 도구
```

## 💡 배운 점 & 개선 경험
- **웹 표준 준수**: 시멘틱 마크업을 통해 브라우저 호환성과 접근성을 고려했습니다.
- **프로젝트 구조 리팩토링**:
    - 초기에는 파일이 산발적으로 흩어져 있었으나, `pages` 및 `assets` 디렉토리를 도입하여 체계적으로 정리했습니다.
    - Python 스크립트를 활용하여 수많은 HTML 파일의 경로 링크(`href`, `src`)를 일괄 수정하는 경험을 했습니다.
- **크로스 플랫폼 호환성 해결**:
    - Windows 환경의 절대 경로 문제를 **상대 경로(`../` 등)**로 전면 수정하여 Mac/Windows 어디서든 정상 작동하도록 개선했습니다.
