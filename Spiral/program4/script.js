function addStudentMarks() {
    const name = document.getElementById('studentName').value;
    const marks = document.getElementById('marks').value;
    if (name && marks) {
        let students = JSON.parse(localStorage.getItem('students')) || [];
        students.push({ name, marks });
        localStorage.setItem('students', JSON.stringify(students));
        alert('Marks added!');
        document.getElementById('studentName').value = '';
        document.getElementById('marks').value = '';
    } else {
        alert('Fill both fields!');
    }
}window.onload = function() {
    const students = JSON.parse(localStorage.getItem('students')) || [];
    const list = document.getElementById('marksList');
    list.innerHTML = students.length ? students.map((s, i) => `
        <li>${s.name} - ${s.marks} <button onclick="deleteStudent(${i})">Delete</button></li>
    `).join('') : '<p>No students found.</p>';
}
function deleteStudent(index) {
    let students = JSON.parse(localStorage.getItem('students')) || [];
    students.splice(index, 1);
    localStorage.setItem('students', JSON.stringify(students));
    alert('Deleted!');
    window.location.reload();
}