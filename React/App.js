import React, {useState, useEffect} from "react"
import api from "./api"

const App = () => {
  const [emner, setEmner] = useState([]);
  const [formData, setFormData] = useState({
    emnekode: "",
    navn: "",
    studiepoeng: "",
    emnekoordinator: ""

  });

const fetchEmner = async () => {
  const response = await api.get("/emner");
  setEmner(response.data)
};

useEffect(() => {
  fetchEmner();
}, []);

const handleInputChange = (event) => {
  const value = event.target.type === "checkbox" ? event.target.checked : event.target.value;
  setFormData({
    ...formData,
    [event.target.name]:value,
  });
};

const handleFormSubmit = async (event) => {
  event.preventDefault();
  await api.post("/emner", formData);
  fetchEmner();
  setFormData({
    emnekode:"",
    navn:"",
    studiepoeng:"",
    emnekoordinator:""
  });
};

return (
  <div>
    <nav className="navbar navbar-dark bg-primary">
      <div className="container-fluid">
        <a className="navbar-brand" href="#">
          Testapplikasjon for intervju
        </a>
      </div>
    </nav>

<div className="container">
  <form onSubmit={handleFormSubmit}>

    <div className="mb-3 mt-3">
      <label htmlFor="emnekode" className="form-label">
        Emnekode
      </label>
      <input type="text" className="form-control" id="emnekode" name="emnekode" onChange={handleInputChange} value={formData.emnekode} />
    </div>

    <div className="mb-3 mt-3">
      <label htmlFor="navn" className="form-label">
        Navn
      </label>
      <input type="text" className="form-control" id="navn" name="navn" onChange={handleInputChange} value={formData.navn} />
    </div>

    <div className="mb-3 mt-3">
      <label htmlFor="amount" className="form-label">
        Studiepoeng
      </label>
      <input type="number" className="form-control" id="studiepoeng" name="studiepoeng" onChange={handleInputChange} value={formData.studiepoeng} />
    </div>

    <div className="mb-3 mt-3">
      <label htmlFor="amount" className="form-label">
        Emnekoordinator
      </label>
      <input type="text" className="form-control" id="emnekoordinator" name="emnekoordinator" onChange={handleInputChange} value={formData.emnekoordinator} />
    </div>

    <button type="submit" className="btn btn-primary">
      Submit
    </button>

  </form>

<table className="table table-striped table-border table-hover">
  <thead>
    <tr>
      <th>Emnekode</th>
      <th>Navn</th>
      <th>Studiepoeng</th>
      <th>Emnekoordinator</th>
    </tr>
  </thead>
  <tbody>
    {emner.map((emne) => (
      <tr key={emne.emnekode}>
        <td>{emne.emnekode}</td>
        <td>{emne.navn}</td>
        <td>{emne.studiepoeng}</td>
        <td>{emne.emnekoordinator}</td>
      </tr>
    ))}
  </tbody>
</table>

</div>




  </div>
)


}



export default App;
