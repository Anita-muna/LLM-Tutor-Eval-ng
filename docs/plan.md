# Plan

**Research question:** How accurate and how helpful are LLM tutors when answering undergraduate computer science questions at Nigerian university level?

**Curriculum basis:** Questions are drawn from the UNIZIK Department of Computer Science course content specifications (CSC101, CSC102, CSC201, CSC202, CSC222, CSC232, CSC252, CSC321, CSC401, CSC431, CSC461).

**Subject areas:** Programming fundamentals, data structures, databases, networking

**Dataset:** About 100 multiple-choice questions I write myself (about 25 per area), based on topics in the UNIZIK curriculum. Each question has four options (A to D) and one correct answer.

**Models:** To decide (3 or 4).

**Method:** Each model answers every question. I score accuracy against my answer key and rate about 30 explanations from 1 to 5 for correctness, clarity, and suitability for an undergraduate student.

**Outputs:** Dataset, scoring script, results table, and a short report (2 to 4 pages) in this repo.