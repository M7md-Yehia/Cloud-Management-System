import os
import tkinter as tk
from tkinter import filedialog, messagebox



def configure_window(root, size="960x540", bg_color="#34405E" ,  title=None):
    window = tk.Toplevel(root)  
    if title:
        window.title(title)  
    window.geometry(size) 
    window.resizable(False, False) 
    window.configure(bg=bg_color)  
    return window  



def open_create_vm_window():
    create_vm_window = configure_window(root, title="Create Virtual Machine")
    cpu_options = ["qemu64", "kvm64", "host"]
    memory_options = ["512", "1024", "2048", "4096", "8192"]
    disk_options = ["10G", "20G", "50G", "100G"]
    tk.Label(create_vm_window, text="CPU:", bg=SUB_BG_COLOR, fg="white").grid(row=0, column=0, padx=10, pady=5)
    cpu_var = tk.StringVar(create_vm_window)
    cpu_var.set(cpu_options[0])
    cpu_menu = tk.OptionMenu(create_vm_window, cpu_var, *cpu_options)
    cpu_menu.grid(row=0, column=1, padx=10, pady=5)
    cpu_menu.configure(bg=SUB_BTN_COLOR)
    tk.Label(create_vm_window, text="Memory (MB):", bg=SUB_BG_COLOR, fg="white").grid(row=1, column=0, padx=10, pady=5)
    memory_var = tk.StringVar(create_vm_window)
    memory_var.set(memory_options[0])
    memory_menu = tk.OptionMenu(create_vm_window, memory_var, *memory_options)
    memory_menu.grid(row=1, column=1, padx=10, pady=5)
    memory_menu.configure(bg=SUB_BTN_COLOR)
    tk.Label(create_vm_window, text="Disk Size (e.g., 10G):", bg=SUB_BG_COLOR, fg="white").grid(row=2, column=0, padx=10, pady=5)
    disk_var = tk.StringVar(create_vm_window)
    disk_var.set(disk_options[0])
    disk_menu = tk.OptionMenu(create_vm_window, disk_var, *disk_options)
    disk_menu.grid(row=2, column=1, padx=10, pady=5)
    disk_menu.configure(bg=SUB_BTN_COLOR)
    tk.Label(create_vm_window, text="ISO Path:", bg=SUB_BG_COLOR, fg="white").grid(row=3, column=0, padx=10, pady=5)
    iso_entry = tk.Entry(create_vm_window)
    iso_entry.grid(row=3, column=1, padx=10, pady=5)
    browse_button = tk.Button(create_vm_window, text="Browse", bg=SUB_BTN_COLOR, command=lambda: browse_iso(iso_entry))
    browse_button.grid(row=3, column=2, padx=10, pady=5)
    create_button = tk.Button(create_vm_window, text="Create VM", bg=SUB_BTN_COLOR, command=lambda: create_vm(cpu_var, memory_var, disk_var, iso_entry, gui_inputs=True))
    create_button.grid(row=4, column=0, columnspan=3, pady=10)

def open_create_dockerfile_window():
    create_dockerfile_window = configure_window(root, title="Create Dockerfile")

    tk.Label(create_dockerfile_window, text="Save Path:", bg=SUB_BG_COLOR, fg="white").grid(row=0, column=0, padx=10, pady=5)
    path_entry = tk.Entry(create_dockerfile_window)
    path_entry.grid(row=0, column=1, padx=10, pady=5)
    browse_button = tk.Button(create_dockerfile_window, text="Browse", bg=SUB_BTN_COLOR, command=lambda: browse_save_path(path_entry))
    browse_button.grid(row=0, column=2, padx=10, pady=5)
    tk.Label(create_dockerfile_window, text="Dockerfile Contents:", bg=SUB_BG_COLOR, fg="white").grid(row=1, column=0, padx=10, pady=5)
    contents_text = tk.Text(create_dockerfile_window, height=10, width=40)
    contents_text.grid(row=2, column=0, columnspan=3, padx=10, pady=5)
    create_button = tk.Button(create_dockerfile_window, text="Create Dockerfile", bg=SUB_BTN_COLOR, command=lambda: create_dockerfile(gui_inputs=True, path_entry=path_entry, contents_text=contents_text))
    create_button.grid(row=3, column=0, columnspan=3, pady=10)

def open_build_docker_image_window():
    build_docker_image_window = configure_window(root, title="Build Docker Image")
    tk.Label(build_docker_image_window, text="Dockerfile Path:", bg=SUB_BG_COLOR, fg="white").grid(row=0, column=0, padx=10, pady=5)
    dockerfile_entry = tk.Entry(build_docker_image_window)
    dockerfile_entry.grid(row=0, column=1, padx=10, pady=5)
    browse_button = tk.Button(build_docker_image_window, text="Browse", bg=SUB_BTN_COLOR, command=lambda: browse_dockerfile(dockerfile_entry))
    browse_button.grid(row=0, column=2, padx=10, pady=5)
    tk.Label(build_docker_image_window, text="Image Name/Tag:", bg=SUB_BG_COLOR, fg="white").grid(row=1, column=0, padx=10, pady=5)
    image_entry = tk.Entry(build_docker_image_window)
    image_entry.grid(row=1, column=1, padx=10, pady=5)
    build_button = tk.Button(build_docker_image_window, text="Build Docker Image", bg=SUB_BTN_COLOR, command=lambda: build_docker_image(gui_inputs=True, dockerfile_entry=dockerfile_entry, image_entry=image_entry))
    build_button.grid(row=2, column=0, columnspan=3, pady=10)

def open_list_docker_images_window():
    list_docker_images_window = configure_window(root, title="List Docker Images")
    images_text = tk.Text(list_docker_images_window, wrap=tk.WORD)
    images_text.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)
    images = list_docker_images()
    images_text.insert(tk.END, images)

def open_list_running_containers_window():
    list_running_containers_window = configure_window(root, title="List Running Containers")
    containers_text = tk.Text(list_running_containers_window, wrap=tk.WORD)
    containers_text.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)
    containers = list_running_containers()
    containers_text.insert(tk.END, containers)

def open_stop_container_window():
    stop_container_window = configure_window(root, title="Stop Docker Container")
    tk.Label(stop_container_window, text="Container ID/Name:", bg=SUB_BG_COLOR, fg="white").grid(row=0, column=0, padx=10, pady=5)
    container_id_entry = tk.Entry(stop_container_window)
    container_id_entry.grid(row=0, column=1, padx=10, pady=5)
    stop_button = tk.Button(stop_container_window, text="Stop Container", bg=SUB_BTN_COLOR, command=lambda: stop_container(gui_inputs=True, container_id_entry=container_id_entry)
)
    stop_button.grid(row=1, column=0, columnspan=2, pady=10)

def open_search_image_window():
    search_image_window = configure_window(root, title="Search Docker Image")
    tk.Label(search_image_window, text="Image Name/Tag:", bg=SUB_BG_COLOR, fg="white").grid(row=0, column=0, padx=10, pady=5)
    image_name_entry = tk.Entry(search_image_window)
    image_name_entry.grid(row=0, column=1, padx=10, pady=5)
    result_text = tk.Text(search_image_window, wrap=tk.WORD)
    result_text.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
    search_button = tk.Button(search_image_window, text="Search Image", bg=SUB_BTN_COLOR, command=lambda: search_image(image_name_entry, result_text))
    search_button.grid(row=2, column=0, columnspan=2, pady=10)

def open_search_image_dockerhub_window():
    search_image_dockerhub_window = configure_window(root, title="Search DockerHub Image")
    tk.Label(search_image_dockerhub_window, text="Image Name/Tag:", bg=SUB_BG_COLOR, fg="white").grid(row=0, column=0, padx=10, pady=5)
    image_name_entry = tk.Entry(search_image_dockerhub_window)
    image_name_entry.grid(row=0, column=1, padx=10, pady=5)
    result_text = tk.Text(search_image_dockerhub_window, wrap=tk.WORD)
    result_text.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
    search_button = tk.Button(search_image_dockerhub_window, text="Search DockerHub", bg=SUB_BTN_COLOR, command=lambda: search_image_dockerhub(image_name_entry, result_text))
    search_button.grid(row=2, column=0, columnspan=2, pady=10)

def open_pull_image_window():
    pull_image_window = configure_window(root, title="Pull Docker Image")
    tk.Label(pull_image_window, text="Image Name/Tag:", bg=SUB_BG_COLOR, fg="white").grid(row=0, column=0, padx=10, pady=5)
    image_name_entry = tk.Entry(pull_image_window)
    image_name_entry.grid(row=0, column=1, padx=10, pady=5)
    pull_button = tk.Button(pull_image_window, text="Pull Image", bg=SUB_BTN_COLOR, command=lambda: pull_image(image_name_entry))
    pull_button.grid(row=1, column=0, columnspan=2, pady=10)



def create_vm(cpu, memory, disk_size, iso_path, gui_inputs=False):
    try:
        if gui_inputs:
            cpu, memory, disk_size, iso_path = cpu.get(), memory.get(), disk_size.get(), iso_path.get()
            if not all([cpu, memory, disk_size, iso_path]):
                return messagebox.showerror("Input Error", "All fields are required")

        os.system(f"qemu-img create -f qcow2 disk_image.qcow2 {disk_size}")
        os.system(f"qemu-system-x86_64 -cpu {cpu} -m {memory} -hda disk_image.qcow2 -cdrom {iso_path} -boot d -no-fd-bootchk")

        if gui_inputs:
            messagebox.showinfo("Success", "Virtual machine created successfully!")
    except Exception as e:
        if gui_inputs:
            messagebox.showerror("Error", f"Failed to create virtual machine: {e}")


def browse_iso(iso_entry):
    filename = filedialog.askopenfilename(title="Select ISO File", filetypes=[("ISO files", "*.iso")])
    if filename:
        iso_entry.delete(0, tk.END)
        iso_entry.insert(0, filename)

def create_dockerfile(path=None, contents=None, gui_inputs=False, path_entry=None, contents_text=None):
    try:
        if gui_inputs:
            path = path_entry.get()
            contents = contents_text.get("1.0", tk.END).strip()
            if not (path and contents):
                return messagebox.showerror("Input Error", "Both fields are required")
        with open(path, 'w') as file:
            file.write(contents)
        if gui_inputs:
            messagebox.showinfo("Success", f"Dockerfile created at {path}")
    except Exception as e:
        if gui_inputs:
            messagebox.showerror("Error", f"Failed to create Dockerfile: {e}")


def browse_save_path(path_entry):
    filename = filedialog.asksaveasfilename(title="Save Dockerfile As", defaultextension=".Dockerfile", filetypes=[("Dockerfile", "*.Dockerfile")])
    if filename:
        path_entry.delete(0, tk.END)
        path_entry.insert(0, filename)

def build_docker_image(dockerfile_path=None, image_name=None, gui_inputs=False, dockerfile_entry=None, image_entry=None):
    try:
        if gui_inputs:
            dockerfile_path, image_name = dockerfile_entry.get(), image_entry.get()
            if not (dockerfile_path and image_name):
                return messagebox.showerror("Input Error", "Both fields are required")
        result = os.popen(f"docker build -t {image_name} -f {dockerfile_path} .").read()
        if gui_inputs:
            messagebox.showinfo("Success", f"Docker image {image_name} built successfully!\n\n{result}")
    except Exception as e:
        if gui_inputs:
            messagebox.showerror("Error", f"Failed to build Docker image: {e}")


def browse_dockerfile(dockerfile_entry):
    filename = filedialog.askopenfilename(title="Select Dockerfile", filetypes=[("Dockerfile", "*.Dockerfile"), ("All Files", "*.*")])
    if filename:
        dockerfile_entry.delete(0, tk.END)
        dockerfile_entry.insert(0, filename)

def list_docker_images():
    try:
        result = os.popen("docker images").read()
        return result
    except Exception as e:
        return f"Error: {e}\nThis error may indicate that the Docker daemon is not running."

def list_running_containers():
    try:
        result = os.popen("docker ps").read()
        return result
    except Exception as e:
        return f"Error: {e}\nThis error may indicate that the Docker daemon is not running."


def stop_container(container_id=None, gui_inputs=False, container_id_entry=None):
    try:
        if gui_inputs:
            container_id = container_id_entry.get()
            if not container_id:
                return messagebox.showerror("Input Error", "Container ID/Name is required")
        result = os.popen(f"docker stop {container_id}").read()
        messagebox.showinfo("Success", f"Container {container_id} stopped successfully!\n\n{result}" if result else f"Container {container_id} stopped successfully!")
    except Exception as e:
        if gui_inputs:
            messagebox.showerror("Error", f"Failed to stop container: {e}")



def search_image(image_name_entry, result_text):
    image_name = image_name_entry.get()
    if not image_name:
        messagebox.showerror("Input Error", "Image name/tag is required")
        return

    try:
        result = os.popen(f"docker images --filter=reference={image_name}").read()
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, result)
    except Exception as e:
        messagebox.showerror("Error", f"Error: {e}\nThis error may indicate that the Docker daemon is not running.")


def search_image_dockerhub(image_name_entry, result_text):
    image_name = image_name_entry.get()
    if not image_name:
        messagebox.showerror("Input Error", "Image name/tag is required")
        return
    try:
        result = os.popen(f"docker search {image_name}").read()
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, result)
    except Exception as e:
        messagebox.showerror("Error", f"Error: {e}\nThis error may indicate that the Docker daemon is not running.")


def pull_image(image_name_entry):
    image_name = image_name_entry.get()
    if not image_name:
        messagebox.showerror("Input Error", "Image name/tag is required")
        return
    try:
        result = os.popen(f"docker pull {image_name}").read()
        messagebox.showinfo("Result", result)
    except Exception as e:
        messagebox.showerror("Error", f"Error: {e}\nThis error may indicate that the Docker daemon is not running.")
        

MAIN_BG_COLOR = "#F0F4FA" 
MAIN_BTN_COLOR = "#4A90E2"  
SUB_BG_COLOR = "#34405E" 
SUB_BTN_COLOR = "#16A015"  

root = tk.Tk()
root.title("QEMU VM Manager")
root.geometry("1440x810")
root.resizable(False, False)
root.configure(bg=MAIN_BG_COLOR)

main_button_vm = tk.Button(root, text="Create Virtual Machine", bg=MAIN_BTN_COLOR, command=open_create_vm_window)
main_button_vm.pack(padx=20, pady=10)

main_button_dockerfile = tk.Button(root, text="Create Dockerfile", bg=MAIN_BTN_COLOR, command=open_create_dockerfile_window)
main_button_dockerfile.pack(padx=20, pady=10)


main_button_build_image = tk.Button(root, text="Build Docker Image", bg=MAIN_BTN_COLOR, command=open_build_docker_image_window)
main_button_build_image.pack(padx=20, pady=10)

main_button_list_images = tk.Button(root, text="List Docker Images", bg=MAIN_BTN_COLOR, command=open_list_docker_images_window)
main_button_list_images.pack(padx=20, pady=10)

main_button_list_running_containers = tk.Button(root, text="List Running Containers", bg=MAIN_BTN_COLOR, command=open_list_running_containers_window)
main_button_list_running_containers.pack(padx=20, pady=10)

main_button_stop_container = tk.Button(root, text="Stop Docker Container", bg=MAIN_BTN_COLOR, command=open_stop_container_window)
main_button_stop_container.pack(padx=20, pady=10)

main_button_search_image = tk.Button(root, text="Search Docker Image", bg=MAIN_BTN_COLOR, command=open_search_image_window)
main_button_search_image.pack(padx=20, pady=10)

main_button_search_image_dockerhub = tk.Button(root, text="Search DockerHub Image", bg=MAIN_BTN_COLOR, command=open_search_image_dockerhub_window)
main_button_search_image_dockerhub.pack(padx=20, pady=10)

main_button_pull_image = tk.Button(root, text="Pull Docker Image", bg=MAIN_BTN_COLOR, command=open_pull_image_window)
main_button_pull_image.pack(padx=20, pady=10)

root.mainloop()
