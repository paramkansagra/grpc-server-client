from concurrent import futures
from time import sleep

from typing import List

import grpc
import employee_pb2
import employee_pb2_grpc


class EmployeeGRPCServicer(employee_pb2_grpc.EmployeeGRPCServicer):
    def __init__(self):
        self.employees: List[employee_pb2.Employee] = []
        self.id = 1

    def addEmployee(self, request: employee_pb2.Employee, context):
        request.id = self.id

        self.employees.append(request)
        self.id += 1

        print("Employee list -> ", self.employees)

        return request

    def getEmployees(self, request: employee_pb2.void, context):
        return employee_pb2.Employees(employees=self.employees)

    def getEmployeesStream(self, request, context):
        for i in self.employees:
            yield i
            sleep(2)


def run():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    employee_pb2_grpc.add_EmployeeGRPCServicer_to_server(EmployeeGRPCServicer(), server)

    server.add_insecure_port("[::]:6969")
    server.start()

    print("starting server at port 6969")

    server.wait_for_termination()


if __name__ == "__main__":
    run()
