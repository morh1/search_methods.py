# Pacman Problem Solver - Readme

## Introduction
This exercise aims to provide hands-on experience in solving variations of the Pacman game using different search methods learned in the course. The game involves guiding Pacman to consume all the dots on the board without being caught by roaming ghosts.

The game board is an NxM grid containing various objects, including walls, Pacman, ghosts, and dots.

## Problem Description
Given the initial state of the game board, represented as an NxM matrix, your task is to implement a Pacman class that can solve the game using the provided search code.

### Objects Representation:
- Wall: `<99>`
- Vulnerable Pacman: `<88>`
- Pacman: `<77>`
- Red Ghost with Pill: `<21>`
- Red Ghost without Pill: `<20>`
- Blue Ghost with Pill: `<31>`
- Blue Ghost without Pill: `<30>`
- Yellow Ghost with Pill: `<41>`
- Yellow Ghost without Pill: `<40>`
- Green Ghost with Pill: `<51>`
- Green Ghost without Pill: `<50>`
- Dotted Tile with Pill: `<11>`
- Empty Tile: `<10>`

## Task Description
You are provided with a search algorithm code (`py1.ex`) that needs to be integrated into the `<PacmanProblem>` class. The following functions must be implemented:

1. `<successor(state)>`: Returns a tuple containing all valid actions from the given state. <br>
2. `<result(state, action)>`: Returns the new state after applying the given action to the current state. <br>
3. `<test_goal(state)>`: Returns `True` if the state is a goal state (Pacman consumed all dots), otherwise `False`. <br>
4. `<h(state)>`: Heuristic function that estimates the cost from the current state to the goal state. <br>
5. `<id>`: Your ID number should be stored in this variable outside the class.

# Code Explanation

## `py1.ex`
This file serves as the main implementation code. It is the sole file that requires modification. 

## `py.check_1ex`
Contained within this file are wrapper functions designed to solve a sample problem. Running this file facilitates testing of your implementation.

## `py.Search`
This file houses search algorithms and the `Node` class, forming the core of the search functionality.

## Other Files
Additional helper files, which play a supporting role in the overall implementation, are present as well.

