#!/usr/bin/env python3
import os
print("=== Python Environment Variables ===")
print(f"TICKTICK_CLIENT_ID: {os.getenv('TICKTICK_CLIENT_ID', 'NOT FOUND')}")
print(f"TICKTICK_CLIENT_SECRET: {os.getenv('TICKTICK_CLIENT_SECRET', 'NOT FOUND')}")
print(f"TICKTICK_ACCESS_TOKEN: {os.getenv('TICKTICK_ACCESS_TOKEN', 'NOT FOUND')}")
print("====================================")
