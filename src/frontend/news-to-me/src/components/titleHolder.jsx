import React, { useState } from 'react';


export const TitleProvider = ({ children }) => {
  const [title, setTitle] = useState("Default Title");

  return (
    <TitleContext.Provider value={{ title, setTitle }}>
      {children}
    </TitleContext.Provider>
  );
};