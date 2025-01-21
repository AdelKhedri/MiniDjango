import sys
from minidjango.core.management.mainmanagement import ManagementSystem


def main():
    manager = ManagementSystem(sys.argv)
    manager.execute()


if __name__ == '__main__':
    main()