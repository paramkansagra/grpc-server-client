import grpc
import employee_pb2
import employee_pb2_grpc


def addEmployee(stub: employee_pb2_grpc.EmployeeGRPCStub):
    id, name, salary = input().split()

    id = int(id)
    salary = float(salary)

    stub.addEmployee(employee_pb2.Employee(id=id, name=name, salary=salary))


def getEmployee(stub: employee_pb2_grpc.EmployeeGRPCStub):
    employee_list: employee_pb2.Employees = stub.getEmployees(employee_pb2.void())

    print(employee_list)


def getEmployeeStream(stub: employee_pb2_grpc.EmployeeGRPCStub):
    print("----Getting as stream----")

    for i in stub.getEmployeesStream(employee_pb2.void()):
        print(i)

    print("----Completed----")


def run():
    with grpc.insecure_channel("[::]:6969") as channel:
        stub = employee_pb2_grpc.EmployeeGRPCStub(channel=channel)

        n = int(input("input the thing you want to do "))
        if n == 1:
            addEmployee(stub=stub)
        elif n == 2:
            getEmployee(stub=stub)
        elif n == 3:
            getEmployeeStream(stub=stub)


if __name__ == "__main__":
    run()
