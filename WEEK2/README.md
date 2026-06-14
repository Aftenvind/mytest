# 接口自动化测试练习项目

## 📋 项目简介

本项目是我从编程教学转型测试开发的学习作品，完整覆盖 RESTful API 自动化测试的核心技术栈。

**学习周期**：2 周（共 14 天）
**技术栈**：Python 3.x + pytest + requests

## 🗂 项目结构

├── conftest.py # 共享 fixture：base_url、api_session、通用断言函数
├── test_api.py # 第一周：GET/POST 基础
├── test_crud.py # 第一周：完整 CRUD（GET/POST/PUT/DELETE）
├── test_param_advanced.py # 第一周：参数化进阶
├── test_data_driven.py # 第一周：数据驱动（外部 JSON）
├── test_auth.py # 第二周：Token 鉴权测试
├── test_posts.py # ★ 综合实战：文章模块 12 条测试
├── test_users.py # ★ 综合实战：用户模块 4 条测试
├── test_todos.py # ★ 综合实战：待办模块 5 条测试
└── requirements.txt # Python 依赖

## 🔧 技能清单

通过本项目，我掌握了以下测试开发核心技能：

| 技能 | 说明 | 对应文件 |
|------|------|----------|
| pytest 基础 | fixture、parametrize、异常测试 | conftest.py, test_api.py |
| requests 接口测试 | GET/POST/PUT/PATCH/DELETE | test_crud.py |
| 数据驱动测试 | JSON 外部文件管理测试数据 | test_data_driven.py |
| Token 鉴权测试 | Authorization Headers 处理 | test_auth.py, test_protected_api.py |
| 测试框架封装 | conftest.py 统一管理 URL/Session/通用断言 | conftest.py |
| 综合实战 | 22+ 条测试覆盖 3 个资源模块 | test_posts/users/todos.py |

## 🚀 如何运行

### 1. 克隆项目
```bash
git clone <你的仓库地址>
cd week2_api_testing