import json
import logging
import os
import shutil
import subprocess
import sys
import time
import pathlib as pl
from datetime import datetime
from json import JSONDecodeError
import mysql.connector as mysql
from mysql.connector import Error
import mandrill