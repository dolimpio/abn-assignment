import axios from 'axios';

const URI = 'http://localhost:8000/data'

// Function to transform the backend data into the desired hierarchical structure
const transformData = (backendData) => {
  const hierarchy = {};

  // Extract the name of the root node from the first element of backendData
  const rootName = backendData.length > 0 ? backendData[0].name : 'Root';
  hierarchy['root'] = { children: [] };

  backendData.forEach(item => {
      const key = item.parent || 'root';
      if (!hierarchy[key]) {
          hierarchy[key] = { children: [] };
      }
      hierarchy[key].children.push({ ...item, children: [] });
  });
  
  const createTree = (parent) => {
      if (!hierarchy[parent]) return null;
      
      return hierarchy[parent].children.map(child => ({
          key: `${parent}_${child.name}`,
          label: child.name,
          data: { description: child.description },
          children: createTree(child.name)
      }));
  };
  
  const tree = createTree('root');

  return {
      key: '0',
      label: rootName, // Set the label dynamically based on the name of the root node
      data: {},
      children: tree
  };
};

export const fetchData = async () => {
    try {
        const response = await axios.get(URI);
        console.log("inside fetch data");
        console.log(response.data)
        // The the data array is under 'data' key
        const responseData = response.data.data; 
        // Convert hierarchy object into array
        const transformedData = transformData(responseData);
        console.log("trasnformed data");
        console.log(transformedData)
        return transformedData;

    } catch (error) {
        console.error('Error fetching data:', error);
        throw error;
    }
};
