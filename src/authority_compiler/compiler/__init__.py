"""Compilation pipeline orchestration.

Responsible for driving the stages -- testimony, evidence, authority,
constitutional checking, and ABI emission -- as a single, ordered pipeline. The
work of each stage lives in that stage's own subpackage.
"""
