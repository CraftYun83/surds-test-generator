fetch("/createProblems", {
    method: "POST"
}).then((data) => {
    data.json().then((d) => {
        d.problems.forEach((problem) => {
            var problemDiv = document.createElement("div")
            problemDiv.classList.add("problem")
            document.body.appendChild(problemDiv)
            katex.render(problem.problem, problemDiv, {
                throwOnError: false
            });

            var answerBtn = document.createElement("button")
            answerBtn.textContent = "Answer"
            answerBtn.onclick = () => {
                if (problemDiv.querySelectorAll("div").length == 0) {
                    var answerDiv = document.createElement("div")
                    problemDiv.appendChild(answerDiv)
                    katex.render("\\text{Answer: }"+problem.answer, answerDiv, {
                        throwOnError: false
                    });
                } else {
                    problemDiv.removeChild(problemDiv.querySelector("div"))
                }
            }

            problemDiv.appendChild(answerBtn)

            if (problem.type == "findhypotenuse") {
                var img = document.createElement("img");
                img.src = "media/problems/P"+problem.id+".png"
                problemDiv.append(img)
                img.addEventListener('load', () => {
                    fetch("deleteMedia/problems/P"+problem.id+".png")
                })
            }
        })
    })
})
