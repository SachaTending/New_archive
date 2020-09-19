import json,os

def addfile(filename, archive):
	with open(archive, 'r') as arch:
		with open(filename, 'r') as file_to_achive:
			data_to_write = {"name": filename, "data": file_to_achive.read()}
		state = json.load(arch)
		os.system("del " + archive)
		state.append(data_to_write)
		arch.close()
	with open(archive, 'w') as arch:
		json.dump(state, arch)

if __name__ == "__main__":
	print("Добавить файл в архив v1.0 BETA")
	while True:
		archive_name = input("Архив(zip и другие не подерживаются(кроме json)):")
		print("Чтение архива....")
		with open(archive_name, 'r') as arch:
			for i in json.load(arch):
				print(i['name'])
		print("Чтение завершено!")
		filenaem_to_archive = input("Файл в архив:")
		print("Добавление файла...")
		addfile(filenaem_to_archive, archive_name)
		print("Добавление завершено!")