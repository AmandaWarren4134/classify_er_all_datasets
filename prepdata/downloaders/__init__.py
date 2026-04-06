"""
Dataset downloaders module for handling different data sources.
"""

try:
    from .base import BaseDownloader
    from .osf_downloader import OSFDownloader

except ImportError:
    # Fallback to absolute imports
    from downloaders.base import BaseDownloader
    from downloaders.osf_downloader import OSFDownloader

__all__ = ['BaseDownloader', 'OSFDownloader']